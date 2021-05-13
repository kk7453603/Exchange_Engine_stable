from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework import filters, status
from main.forms import LeverageTradingForm, UserBalance
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Stocks, Order, Portfolio, User, Quotes, LeverageData, Statistics, Candles
from main import serializers

from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


@api_view(['POST',])
def registration_view(request):
    """
    Регистрация
    """
    if request.method == 'POST':
        serializer = serializers.RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "succefully"
            data['email'] = account.email
            data['username'] = account.username
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data)


class AddOrderView(APIView):
    """
    Добавление ордера

    :param price: Цена ордера
    :param stock: Имя акции
    :param type: Тип ордера
    :param amount: Количество ордеров
    """
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def margin_call(user):
        """
        Margin call
        """
        if LeverageData.objects.filter(user=user):
            user_data = LeverageData.objects.get(user=user)
            if user.balance <= 0:
                for object in Order.objects.filter(user=user, stock=user_data.stock):
                    object.is_closed = True
                    object.save()

    @staticmethod
    def set_percentage(user_portfolio):
        """
        Установка процента в портфолио
        """
        sum = 0
        portfolios = Portfolio.objects.filter(stock_id=user_portfolio.stock_id)
        for object in portfolios:
                sum += object.count
        if sum == 0:
            per_stocks = 100
        else:
            per_stocks = (user_portfolio.count / sum) * 100
        user_portfolio.percentage = per_stocks
        user_portfolio.save()

    def post(self, request):
        """
        Добавление акции и обработка данных при POST запросе
        """
        data = request.data
        user = request.user
        name = data['stock']
        stock = Stocks.objects.get(name=name)
        type = data['type']
        price = float(data['price'])
        amount = int(data['amount'])
        if price <= 0 or amount <= 0:
            return Response({"detail": "uncorrect data"}, status=status.HTTP_400_BAD_REQUEST)
        self.margin_call(user)
        portfolio, created = Portfolio.objects.get_or_create(user=user, stock=stock)
        self.set_percentage(portfolio)
        order = Order(user=user, stock=stock, type=type, price=price, is_closed=False, amount=amount)
        order_ops = Order.objects.filter(stock=stock, type=not type, price=price, is_closed=False)
        for order_op in order_ops:
            if order.amount != 0:
                user_op = order_op.user
                portfolio_op = Portfolio.objects.get(user=user_op, stock=stock)

                min_count = min(order.amount, order_op.amount) if type == 0 else -min(order.amount, order_op.amount)

                order.amount -= abs(min_count)
                order_op.amount -= abs(min_count)

                portfolio.count += min_count
                portfolio_op.count -= min_count

                user_op.balance += min_count * price
                user.balance -= min_count * price

                if portfolio.count < 0:
                    portfolio.short_balance -= min_count * price
                    user.balance += min_count * price
                    portfolio.is_debt = True

                if portfolio_op.count < 0:
                    portfolio_op.short_balance += min_count * price
                    user_op.balance -= min_count * price
                    portfolio_op.is_debt = True

                if portfolio.count == 0 and portfolio.is_debt:
                    user.balance += 100000 + portfolio.short_balance
                    portfolio.short_balance = -100000
                    portfolio.is_debt = False

                if portfolio_op.count == 0 and portfolio_op.is_debt:
                    user.balance += 100000 + portfolio.short_balance
                    portfolio_op.short_balance = -100000
                    portfolio_op.is_debt = False

                if order_op.amount == 0:
                    order_op.is_closed = True
                    order_op.date_closed = timezone.now()

                self.margin_call(user)
                self.margin_call(user_op)
                self.set_percentage(portfolio)
                self.set_percentage(portfolio_op)

                user_op.save()
                order_op.save()
                portfolio_op.save()
            if order.amount == 0:
                order.is_closed = True
                order.date_closed = timezone.now()

        user.save()
        portfolio.save()
        order.save()
        return Response("/api/v1/orders/")


class StocksListView(ListAPIView):
    """
    Список акций
    """
    queryset = Stocks.objects.filter(is_active=True)
    serializer_class = serializers.StocksSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']


class StockDetailView(APIView):
    """
    Информация об акции
    """

    def get(self, request, pk):
        """
        Отображение данных о конкретной акции при GET запросе
        """
        stock = Stocks.objects.get(id=pk)
        serializer = serializers.StocksSerializer(stock)
        return Response(serializer.data)


class StatisticsView(APIView):
    """
    Статистика биржи
    """
    def get(self, request):
        open_orders = 0
        closed_orders = 0
        user_active = 0
        count_stocks = 0
        count_long = 0
        count_short = 0
        max_balance = 0
        the_richest = ''

        id_admin = User.objects.get(username='admin')
        orders = Order.objects.all()
        users = User.objects.all()
        stocks = Stocks.objects.all()
        portfolio = Portfolio.objects.all()
        for order in orders:
            if order.is_closed:
                if order.user_id != id_admin.id:
                    open_orders += 1
            else:
                if order.user_id != id_admin.id:
                    closed_orders += 1

        for user in users:
            if user.is_active:
                user_active += 1
            if user.balance > max_balance:
                if user.username != 'admin':
                    max_balance = user.balance
                    the_richest = user.username

        for stock in stocks:
            if stock.is_active:
                count_stocks += 1

        for port in portfolio:
            if port.short_balance == -100000:
                if port.user_id != id_admin.id:
                    count_long += 1
            else:
                if port.user_id != id_admin.id:
                    count_short += 1

        name = 'orders_count'

        try:
            statistics = Statistics.objects.get(name=name)
            statistics.open_orders = open_orders
            statistics.user_active = user_active
            statistics.closed_orders = closed_orders
            statistics.count_stocks = count_stocks
            statistics.count_short = count_short
            statistics.count_long = count_long
            statistics.max_balance = max_balance
            statistics.the_richest = the_richest
            statistics.save()
        except ObjectDoesNotExist:
            Statistics.objects.create(name=name, open_orders=open_orders, closed_orders=closed_orders, user_active=user_active,\
                                      count_stocks=count_stocks, count_long=count_long, count_short=count_short, max_balance=max_balance,\
                                      the_richest=the_richest)
        statistics = Statistics.objects.all()
        serializer = serializers.StatisticsSerializer(statistics, many=True)
        return Response(serializer.data)


class ProfileDetailView(APIView):
    """
        Информация о пользователе

        :param profile: Профиль
        :param avatar: Аватарка пользователяstatistics = Statistics(open_orders=open_orders, closed_orders=closed_orders)
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        Отображение профиля пользователя при GET запросе
        """
        user = request.user
        return Response(serializers.ProfileDetailSerializer(user).data)

    def patch(self, request):
        """
        Заполнение профиля
        """
        user = request.user
        data = request.data

        user.email = data.get("email", user.email)
        user.first_name = data.get("first_name", user.first_name)
        user.last_name = data.get("last_name", user.last_name)
        password2 = data.get("password2", user.password)
        if password2:
            if user.check_password(data.get("password", user.password)):
                user.set_password(password2)
            # else:
            #     return Response({"detail": "password must match"}, status=status.HTTP_400_BAD_REQUEST)

        if request.FILES:
            user.avatar = request.FILES['file']

        user.save()
        serializer = serializers.ProfileDetailSerializer(user)

        return Response(serializer.data)

class CandlesView(APIView):
    """
    Свечи
    """
    def get(self, request, pk):
        """
        Отображение всех ордеров пользователя при GET запросе
        """
        candles = Candles.objects.filter(stock_id=pk)
        serializer = serializers.CandlesSerializer(candles, many=True)
        return Response(serializer.data)

class OrdersView(APIView):
    """
    Все заявки пользователя
    """

    def get(self, request):
        """
        Отображение всех ордеров пользователя при GET запросе
        """
        user = request.user
        orders = Order.objects.filter(user_id=user)
        serializer = serializers.OrdersSerializer(orders, many=True)
        return Response(serializer.data)


class PortfolioUserView(APIView):
    """
    Портфолио пользователя
    """

    def get(self, request):
        """
        Отображение портфолио пользователя при GET запросе
        """
        portfolio = Portfolio.objects.filter(~Q(count=0), user_id=request.user.id,)
        serializer = serializers.PortfolioUserSerializer(portfolio, many=True)
        return Response(serializer.data)


class LeverageTradingView(APIView):
    """
    Торговля с плечом
    """

    def get(self, request):
        """
        Отображение формы при GET запросе
        """
        form = LeverageTradingForm(initial={
            'type': 0,
            'stock': 0,
            'ratio': 2,
        })
        user = User.objects.get(id=request.user.pk)
        context = {
            'user': user,
            'form': form,
            'too_low': 0,
        }
        return render(request, 'trading/leverage.html', context)

    def post(self, request):
        """
        Торговля с плечом и обработка данных при POST запросе
        """
        form = LeverageTradingForm(request.POST)

        user = User.objects.get(id=request.user.pk)
        ratio = int(request.POST.get('ratio'))
        stock = Stocks.objects.get(name=request.POST.get('stock'))
        quote = Quotes.objects.filter(stock=stock.id).last()
        type = True if request.POST.get('type') else False
        cash = user.balance * ratio
        AddOrderView.margin_call(user)
        if cash // quote.price >= 1:
            amount = cash // quote.price
            try:
                broker = LeverageData.objects.get(user=user, stock=stock)
                order = Order.objects.get(user=user, stock=stock, type=type, price=quote.price, is_closed=False)
                order.amount = amount
                broker.ratio = ratio
            except LeverageData.DoesNotExist:
                broker = LeverageData(user=user, stock=stock, ratio=ratio)
                order = Order(user=user, stock=stock, type=type, price=quote.price, is_closed=False, amount=amount)
            order.save()
            broker.save()
            return HttpResponseRedirect("/api/v1/orders/")
        else:
            context = {
                'too_low': 1,
                'form': form,
            }
            return render(request, 'trading/leverage.html', context)


class ProfileBalanceAdd(APIView):
    """
    Пополнение баланса пользователя
    """

    def get(self, request):
        """
        Отображение формы для пополнения баланса пользователя при GET запросе
        """
        context = {}
        form = UserBalance()
        context['form'] = form
        return render(request, 'profile/balance_add.html', context)

    def post(self, request):
        """
        Пополение баланса пользователя и обработка данных при POST запросе
        """
        form = UserBalance(request.POST)
        user = User.objects.get(id=request.user.pk)
        if form.is_valid():
            context = {'form': form}
            money = request.POST['money']
            try:
                user.balance = float(money.replace(',', '.', 1)) + float(user.balance)
                user.save()
                return render(request, 'profile/balance_add_successfully.html', context)
            except ValueError:
                return render(request, 'profile/balance_add_failed.html')
        return render(request, 'profile/balance_add_failed.html')


class PricesView(APIView):
    """
    Страница с текущими и предыдущими котировками акций
    """
    def get(self, request):
        """
        Отображение всех котировок акций при GET запросе
        """
        prices = Quotes.objects.all()
        serializer = serializers.PriceSerializer(prices, many=True)
        return Response(serializer.data)
