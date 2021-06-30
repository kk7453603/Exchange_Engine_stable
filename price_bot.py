import os
import time
from datetime import datetime
from math import sin, pi
from django.utils import timezone
from random import randint, choice, random, uniform
import django
import pandas
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exchange_engine.settings')
django.setup()

from main.models import Stocks, Order, User, Quotes, Portfolio, Settings, LeverageData

NEED_RESTART = False


class CrisisFigureOne:
    @staticmethod
    def generate(_price, stock_id):
        price = _price - _price * uniform(0.06667, 0.12245310)
        price = HandlingFunctions.check_price(price, stock_id)
        return price


class CrisisFigureTwo:
    @staticmethod
    def generate(_price, stock_id):
        price = _price - _price * uniform(0.08766755, 0.15809768576)
        price = HandlingFunctions.check_price(price, stock_id)
        return price


class CrisisFigureThree:
    @staticmethod
    def generate(_price, stock_id):
        price = _price - _price * uniform(0.15345336, 0.2578978)
        price = HandlingFunctions.check_price(price, stock_id)
        return price


class NeutralFigureOne:
    @staticmethod
    def generate(_price, stock_id):
        price = _price - _price * 0.015
        price = HandlingFunctions.check_price(price, stock_id)
        return price


class NeutralFigureTwo:
    @staticmethod
    def generate(_price, stock_id):
        price = _price + _price * 0.015
        price = HandlingFunctions.check_price(price, stock_id)
        return price


class DowngradingFigureOne:
    @staticmethod
    def generate(_price, stock_id):
        cut = uniform(0.64, 4.03) * pi / 180
        price = _price - _price * sin(cut)
        price = HandlingFunctions.check_price(price, stock_id)
        return price


class DowngradingFigureTwo:
    @staticmethod
    def generate(_price, stock_id):
        cut = uniform(0.84, 4.27) * pi / 180
        price = _price - _price * sin(cut) * random()
        price = HandlingFunctions.check_price(price, stock_id)
        return price


class DowngradingFigureThree:
    @staticmethod
    def generate(_price, stock_id):
        cut = uniform(1, 3.86) * pi / 180
        price = _price - _price * sin(cut) * uniform(0.67, 0.99)
        price = HandlingFunctions.check_price(price, stock_id)
        return price


class DowngradingFigureFour:
    @staticmethod
    def generate(_price, stock_id):
        price = _price - _price * uniform(0.02, 0.055)
        price = HandlingFunctions.check_price(price, stock_id)
        return price


class RaisingFigureOne:
    @staticmethod
    def generate(_price, stock_id):
        cut = uniform(0.64, 4.03) * pi / 180
        price = _price + _price * sin(cut)
        price = HandlingFunctions.check_price(price, stock_id)
        return price


class RaisingFigureTwo:
    @staticmethod
    def generate(_price, stock_id):
        cut = uniform(0.84, 4.27) * pi / 180
        price = _price + _price * sin(cut) * random()
        price = HandlingFunctions.check_price(price, stock_id)
        return price


class RaisingFigureThree:
    @staticmethod
    def generate(_price, stock_id):
        cut = uniform(1, 3.86) * pi / 180
        price = _price + _price * sin(cut) * uniform(0.67, 0.99)
        price = HandlingFunctions.check_price(price, stock_id)
        return price


class RaisingFigureFour:
    @staticmethod
    def generate(_price, stock_id):
        price = _price + _price * uniform(0.02, 0.055)
        price = HandlingFunctions.check_price(price, stock_id)
        return price


class Figures:
    @staticmethod
    def set_figures(du, tendency):
        raising_figures = [RaisingFigureOne, RaisingFigureTwo, RaisingFigureThree, RaisingFigureFour]
        neutral_figures = [NeutralFigureOne, NeutralFigureTwo]
        downgrading_figures = [DowngradingFigureOne, DowngradingFigureTwo, DowngradingFigureThree,
                               DowngradingFigureFour]
        data = []
        figures = []
        duration = []
        if tendency == 'raising':
            for i in range(du):
                figures.append(choice(raising_figures))
            for i in range(len(figures)):
                randomized = randint(1, 10)
                if randomized <= 3:
                    figures.insert(i, choice(downgrading_figures))
                elif 6 >= randomized >= 3:
                    figures.insert(i, choice(neutral_figures))
        elif tendency == 'downgrading':
            for i in range(du):
                figures.append(choice(downgrading_figures))
            for i in range(len(figures)):
                randomized = randint(1, 10)
                if randomized <= 3:
                    figures.insert(i, choice(raising_figures))
                elif 6 >= randomized >= 3:
                    figures.insert(i, choice(neutral_figures))
        for i in figures:
            duration.append(randint(2, 6))
        data.append(figures)
        data.append(duration)
        return data

    @staticmethod
    def get_figure(f_t):
        crisis_figures = [CrisisFigureOne, CrisisFigureTwo, CrisisFigureThree]
        raising_figures = [RaisingFigureOne, RaisingFigureTwo, RaisingFigureThree, RaisingFigureFour]
        neutral_figures = [NeutralFigureOne, NeutralFigureTwo]
        downgrading_figures = [DowngradingFigureOne, DowngradingFigureTwo, DowngradingFigureThree,
                               DowngradingFigureFour]
        randomized = 0
        num = randint(1, 13)
        if f_t == 'raising':
            if 13 >= num >= 10:
                randomized = choice(neutral_figures)
            else:
                randomized = choice(raising_figures)
        elif f_t == 'downgrading':
            if 13 >= num >= 10:
                randomized = choice(neutral_figures)
            else:
                randomized = choice(downgrading_figures)
        elif f_t == 'crisis':
            randomized = choice(crisis_figures)
        return randomized


class HandlingFunctions:

    @staticmethod
    def limits_check(stock_id, min_price, max_price):
        global NEED_RESTART
        quotes = list(Quotes.objects.filter(stock_id=stock_id))
        if len(quotes) > 1:
            shift = 0
            edited = list(reversed(quotes))
            for i in range(len(edited)):
                if i + 1 < len(edited):
                    if edited[i].price > max_price:
                        shift += (edited[i].date - edited[i+1].date).total_seconds()
                        if shift >= 15:
                            NEED_RESTART = True
                            shift = 0
                    elif edited[i].price < min_price:
                        shift += (edited[i].date - edited[i+1].date).total_seconds()
                        if shift >= 15:
                            NEED_RESTART = True
                            shift = 0

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
    def limit_order_update():
        orders = Order.objects.filter(is_limit=True, is_closed=False)
        for order in orders:
            stock = Stocks.objects.get(id=order.stock_id)
            if Settings.objects.filter(stock_id=-1, name='short_switch'):
                setting = Settings.objects.filter(stock_id=-1, name='short_switch').last()
            elif Settings.objects.filter(stock_id=stock.id, name='short_switch'):
                setting = Settings.objects.filter(stock_id=stock.id, name='short_switch').last()
            type = order.type
            portfolio = Portfolio.objects.get(user_id=order.user_id, stock=order.stock_id)
            user = User.objects.get(id=order.user_id)
            if order.amount != 0:
                if order.is_limit:

                    if order.type == 0:
                        print(stock.price, order.price)
                        if stock.price <= order.price:
                            print(
                                "5555555555555555555555555555555555555555555")
                            order.is_limit = False


                            if type == 0 and not portfolio.is_debt:
                                print(
                                    "6666666666666666666666666666666666666666666666")
                                if user.balance >= order.amount * order.price:

                                    portfolio.count += order.amount
                                    user.balance -= order.amount * order.price
                                else:
                                    # обработать ошибку не хватки денег
                                    return Response({"detail": "incorrect data"},tatus=status.HTTP_400_BAD_REQUEST)


                            elif type == 1 and portfolio.count >= order.amount and not portfolio.is_debt:

                                portfolio.count -= order.amount
                                user.balance += order.amount * stock.price


                            elif type == 1 and portfolio.count == 0 and not portfolio.is_debt:
                                if (setting is None or setting.data['is_active']) or not setting.data['is_active']:
                                    if order.amount * order.price <= 100000 and portfolio.short_balance <= 0:
                                        portfolio.short_balance += order.amount * order.price
                                        portfolio.is_debt = True
                                        portfolio.count = -order.amount
                                    else:
                                        # обработать ошибку нельзя торговать шорт при захождении заграницу
                                        return Response({"detail": "incorrect data"},
                                                        status=status.HTTP_400_BAD_REQUEST)
                                else:
                                    # торговать в шорт не возможно
                                    return Response({"detail": "incorrect data"},
                                                    status=status.HTTP_400_BAD_REQUEST)
                            elif type == 1 and portfolio.count < order.amount and portfolio.count != 0 and not portfolio.is_debt:
                                if setting.data['is_active']:
                                    if (order.amount - portfolio.count) * order.price <= 100000 and portfolio.short_balance <= 0:
                                        user.balance += portfolio.count * stock.price  # цена на данный момент
                                        portfolio.is_debt = True
                                        portfolio.count = portfolio.count - order.amount
                                        portfolio.short_balance -= portfolio.count * stock.price

                                    else:
                                        # обработать ошибку нельзя торговать шорт при захождении заграницу
                                        return Response({"detail": "incorrect data"},
                                                        status=status.HTTP_400_BAD_REQUEST)
                                else:
                                    # торговать в шорт не возможно
                                    return Response({"detail": "incorrect data"},
                                                    status=status.HTTP_400_BAD_REQUEST)

                            elif type == 1 and portfolio.is_debt:
                                if order.amount * order.price <= 100000 and portfolio.short_balance <= 0:
                                    portfolio.short_balance += order.amount * order.price
                                    portfolio.count -= order.amount
                                else:
                                    # торговать в шорт не возможно
                                    return Response({"detail": "incorrect data"},
                                                    status=status.HTTP_400_BAD_REQUEST)

                            elif type == 0 and portfolio.is_debt and portfolio.count < -order.amount:
                                user.balance += (100000 - portfolio.short_balance) - order.amount * stock.price
                                portfolio.count += order.amount

                            elif type == 0 and portfolio.is_debt and portfolio.count == -order.amount:
                                user.balance += (100000 - portfolio.short_balance) - order.amount * stock.price
                                portfolio.count = 0
                                portfolio.is_debt = False

                            elif type == 0 and portfolio.is_debt and portfolio.count > -order.amount:
                                if order.amount + portfolio.count * order.price < user.balance:
                                    user.balance += (
                                                            100000 - portfolio.short_balance) - portfolio.count * stock.price
                                    portfolio.count = order.amount + portfolio.count
                                    portfolio.is_debt = False
                                    user.balance -= portfolio.count * order.price
                                else:
                                    # обработать ошибку не хватки денег
                                    return Response({"detail": "incorrect data"},
                                                    status=status.HTTP_400_BAD_REQUEST)

                            order.is_closed = True
                            order.date_closed = timezone.now()
                            user.save()
                            order.save()
                            portfolio.save()

                        HandlingFunctions.margin_call(user)
                        sred = portfolio.count
                        portfolio.aver_price = ((sred * (sred - order.amount)
                                                 + abs(order.amount) * order.price) / max(abs(sred), 1) * bool(
                            sred))
                    else:

                        if stock.price >= order.price:

                            order.is_limit = False


                            if type == 0 and not portfolio.is_debt:

                                if user.balance >= order.amount * order.price:

                                    portfolio.count += order.amount
                                    user.balance -= order.amount * order.price
                                    user.save()
                                    portfolio.save()
                                else:
                                    # обработать ошибку не хватки денег
                                    return Response({"detail": "incorrect data"},
                                                    status=status.HTTP_400_BAD_REQUEST)

                            elif type == 1 and portfolio.count >= order.amount and not portfolio.is_debt:

                                portfolio.count -= order.amount
                                user.balance += order.amount * stock.price
                                user.save()
                                portfolio.save()


                            elif type == 1 and portfolio.count == 0 and not portfolio.is_debt:
                                if (setting is None or setting.data['is_active']) or not setting.data['is_active']:
                                    if order.amount * order.price <= 100000:
                                        portfolio.short_balance += order.amount * order.price
                                        portfolio.is_debt = True
                                        portfolio.count = -order.amount
                                        portfolio.save()
                                    else:
                                        # обработать ошибку нельзя торговать шорт при захождении заграницу
                                        return Response({"detail": "incorrect data"},
                                                        status=status.HTTP_400_BAD_REQUEST)
                                else:
                                    # торговать в шорт не возможно
                                    return Response({"detail": "incorrect data"},
                                                    status=status.HTTP_400_BAD_REQUEST)
                            elif type == 1 and portfolio.count < order.amount and portfolio.count != 0 and not portfolio.is_debt:
                                if setting.data['is_active']:
                                    if (order.amount - portfolio.count) * order.price <= 100000:
                                        user.balance += portfolio.count * stock.price  # цена на данный момент
                                        portfolio.is_debt = True
                                        portfolio.count = portfolio.count - order.amount
                                        portfolio.short_balance -= portfolio.count * stock.price
                                        user.save()
                                        portfolio.save()
                                    else:
                                        # обработать ошибку нельзя торговать шорт при захождении заграницу
                                        return Response({"detail": "incorrect data"},
                                                        status=status.HTTP_400_BAD_REQUEST)
                                else:
                                    # торговать в шорт не возможно
                                    return Response({"detail": "incorrect data"},
                                                    status=status.HTTP_400_BAD_REQUEST)

                            elif type == 1 and portfolio.is_debt:
                                if order.amount * order.price <= 100000:
                                    portfolio.short_balance += order.amount * order.price
                                    portfolio.count -= order.amount
                                    user.save()
                                    portfolio.save()

                            elif type == 0 and portfolio.is_debt and portfolio.count < -order.amount:
                                user.balance += (100000 - portfolio.short_balance) - order.amount * stock.price
                                portfolio.count += order.amount
                                user.save()
                                portfolio.save()

                            elif type == 0 and portfolio.is_debt and portfolio.count == -order.amount:
                                user.balance += (100000 - portfolio.short_balance) - order.amount * stock.price
                                portfolio.count = 0
                                portfolio.is_debt = False
                                user.save()
                                portfolio.save()

                            elif type == 0 and portfolio.is_debt and portfolio.count > -order.amount:
                                if order.amount + portfolio.count * order.price < user.balance:
                                    user.balance += (
                                                            100000 - portfolio.short_balance) - portfolio.count * stock.price
                                    portfolio.count = order.amount + portfolio.count
                                    portfolio.is_debt = False
                                    user.balance -= portfolio.count * order.price
                                    user.save()
                                    portfolio.save()
                                else:
                                    # обработать ошибку не хватки денег
                                    return Response({"detail": "incorrect data"},
                                                    status=status.HTTP_400_BAD_REQUEST)

                            order.is_closed = True
                            order.date_closed = timezone.now()
                            order.save()
                            portfolio.save()

                        HandlingFunctions.margin_call(user)
                        sred = portfolio.count
                        portfolio.aver_price = ((sred * (sred - order.amount)
                                                 + abs(order.amount) * order.price) / max(abs(sred), 1) * bool(
                            sred))



    @staticmethod
    def get_settings(stock_id):
        if Settings.objects.filter(stock_id=-1, name='algo_quotes'):
            setting = Settings.objects.filter(stock_id=-1, name='algo_quotes').last()
            return setting
        elif Settings.objects.filter(stock_id=stock_id, name='algo_quotes'):
            setting = Settings.objects.filter(stock_id=stock_id, name='algo_quotes').last()
            return setting
        return None

    @staticmethod
    def get_timer(stock_id):
        setting = None
        if Settings.objects.filter(stock_id=-1, name='frequency_generating_quotes'):
            setting = Settings.objects.filter(stock_id=-1, name='frequency_generating_quotes').last()
        elif Settings.objects.filter(stock_id=stock_id, name='frequency_generating_quotes'):
            setting = Settings.objects.filter(stock_id=stock_id, name='frequency_generating_quotes').last()
        if setting is not None:
            timer = setting.data['timer']
        else:
            timer = 30
        return timer

    @staticmethod
    def get_pause(stock_id):
        setting = None
        if Settings.objects.filter(stock_id=-1, name='quotes_generation_switch'):
            setting = Settings.objects.filter(stock_id=-1, name='quotes_generation_switch').last()
        elif Settings.objects.filter(stock_id=stock_id, name='quotes_generation_switch'):
            setting = Settings.objects.filter(stock_id=stock_id, name='quotes_generation_switch').last()
        if setting is None:
            return False
        elif setting.data['is_stop']:
            return True
        else:
            return False

    @staticmethod
    def get_last_price(stock):
        if Quotes.objects.filter(stock=stock):
            last_price = Quotes.objects.filter(stock=stock).last().price
        else:
            last_price = randint(42, 5000)
        return last_price

    @staticmethod
    def generate_orders(user, stock, price, AMOUNT, line=-1):
        Order.objects.create(user=user, stock=stock, type=True, price=price, amount=AMOUNT, is_closed=True)
        Order.objects.create(user=user, stock=stock, type=False, price=price, amount=AMOUNT, is_closed=True)
        Order.objects.create(user=user, stock=stock, type=True, price=price, amount=AMOUNT * 10, is_closed=False)
        Order.objects.create(user=user, stock=stock, type=False, price=price, amount=AMOUNT * 10, is_closed=False)
        Quotes.objects.create(stock=stock, price=price, line=line)
        stock.price = price
        stock.save()
        portfolio, created = Portfolio.objects.get_or_create(user=user, stock=stock)
        portfolio.count = 100000
        portfolio.save()
        HandlingFunctions.limit_order_update()
    @staticmethod
    def check_price(_price, stock_id):
        setting = HandlingFunctions.get_settings(stock_id)
        max_price = 15000
        min_price = 500
        if setting is not None and setting.data['max_price'] is not None and setting.data['min_price'] is not None:
            max_price = setting.data['max_price']
            min_price = setting.data['min_price']
            if _price > max_price:
                _price = max_price - max_price * uniform(0.03, 0.1)
            elif _price < min_price:
                _price = min_price + min_price * uniform(0.03, 0.1)
        else:
            if _price > max_price:
                _price = max_price - max_price * uniform(0.03, 0.1)
            elif _price < min_price:
                _price = min_price + min_price * uniform(0.03, 0.1)
        HandlingFunctions.limits_check(stock_id, min_price, max_price)
        return _price


class Tendencies:
    @staticmethod
    def choose_tendency():
        data = []
        tendencies = ['raising', 'downgrading']
        data.append(choice(tendencies))
        data.append(randint(5, 10))
        data.append([])
        return data

    @staticmethod
    def settings_check(stock, user, AMOUNT, last_price, t):
        if HandlingFunctions.get_settings(stock.id) is not None:
            setting = HandlingFunctions.get_settings(stock.id)
            if setting.data['start_after_time'] is not None:
                if setting.data['start_after_time'] > 0:
                    setting.data['start_after_time'] -= t
                elif setting.data['duration'] is not None:
                    if setting.data['duration'] > 0:
                        setting.data['duration'] -= t
                        if setting.data['type'] is not None:
                            coefficient = setting.data['coefficient']
                            f_type = setting.data['type']
                            figure = Figures.get_figure(f_type)
                            price = figure.generate(last_price, stock.id) * coefficient
                            HandlingFunctions.generate_orders(user, stock, price, AMOUNT, t)
                    elif setting.data['duration'] <= 0:
                        return False
            elif setting.data['coefficient'] is not None and setting.data['type'] is None:
                return False

            elif setting.data['duration'] is not None:
                if setting.data['duration'] > 0:
                    setting.data['duration'] -= t
                    if setting.data['type'] is not None:
                        coefficient = setting.data['coefficient']
                        f_type = setting.data['type']
                        figure = Figures.get_figure(f_type)
                        price = figure.generate(last_price, stock.id) * coefficient
                        HandlingFunctions.generate_orders(user, stock, price, AMOUNT, t)
                elif setting.data['duration'] <= 0:
                    return False
            elif setting.data['coefficient'] is not None and setting.data['type'] is None:
                return False

            setting.save()
            return True
        else:
            return False

    @staticmethod
    def opposite_tendency(tendency):
        if tendency == 'raising':
            tendency = 'downgrading'
        elif tendency == 'downgrading':
            tendency = 'raising'
        return tendency


class MainCycle:
    @staticmethod
    def begin(am, us):
        global NEED_RESTART
        is_frozen = False
        user = us
        AMOUNT = am
        t = 30
        stocks = Stocks.objects.all()
        data = [['none', 0, []] for _ in range(len(Stocks.objects.all()))]
        while True:
            for stock in stocks:
                info = data[stock.pk - 1]
                tendency = info[0]
                duration = info[1]
                last_price = HandlingFunctions.get_last_price(stock)
                t = HandlingFunctions.get_timer(stock.pk)
                is_frozen = HandlingFunctions.get_pause(stock.pk)
                if not is_frozen:
                    if not Tendencies.settings_check(stock, user, AMOUNT, last_price, t):
                        if duration == 0:
                            info = Tendencies.choose_tendency()
                            data[stock.pk - 1] = info
                        else:
                            if info[2] == []:
                                info[2] = Figures.set_figures(duration, tendency)
                            else:
                                pack = []
                                figures = info[2][0]
                                duration = info[2][1]
                                index = next((x for x in range(len(duration)) if duration[x] > 0), 'not found')
                                if index == 'not found':
                                    info[1] = 0
                                else:
                                    duration[index] -= 1
                                    if HandlingFunctions.get_settings(stock.pk) is not None and \
                                        HandlingFunctions.get_settings(stock.pk).data['coefficient'] is not None:
                                        coef = HandlingFunctions.get_settings(stock.pk).data['coefficient']
                                        price = figures[index].generate(last_price, stock.id) * coef
                                        if not NEED_RESTART:
                                            HandlingFunctions.generate_orders(user, stock, price, AMOUNT, t)
                                        else:
                                            f_tendency = info[0]
                                            info = Tendencies.choose_tendency()
                                            data[stock.pk - 1] = info
                                            info[0] = Tendencies.opposite_tendency(f_tendency)
                                            info[2] = Figures.set_figures(info[1], tendency)
                                            NEED_RESTART = False
                                            HandlingFunctions.generate_orders(user, stock, price, AMOUNT, t)
                                    else:
                                        price = figures[index].generate(last_price, stock.id)
                                        if not NEED_RESTART:
                                            HandlingFunctions.generate_orders(user, stock, price, AMOUNT, t)
                                        else:
                                            f_tendency = info[0]
                                            info = Tendencies.choose_tendency()
                                            data[stock.pk - 1] = info
                                            info[0] = Tendencies.opposite_tendency(f_tendency)
                                            info[2] = Figures.set_figures(info[1], tendency)
                                            NEED_RESTART = False
                                            HandlingFunctions.generate_orders(user, stock, price, AMOUNT, t)
                                pack.append(figures)
                                pack.append(duration)
                                info[2] = pack
            if data[0][2] != []:
                time.sleep(t)


def price_bot():
    logging.basicConfig(format='', level=logging.INFO)
    try:
        logging.info('Бот начал работу')
        files = next(os.walk('data/'))[2]
        min_file_length = min([len(open(f'data/{file}', 'r').readlines()) for file in files])
        user = User.objects.get(username='admin')
        AMOUNT = 10000
        is_frozen = False
        settings_interruption = 0
        timer = 30
        is_exist = False
        for i in range(min_file_length - 1):
            if not is_frozen:
                if settings_interruption == 0:
                    for file in files:
                        df = pandas.read_csv(f'data/{file}', nrows=1, skiprows=i, sep=';')
                        name = df.iloc[0][0]
                        if name[len(name) - 3:] != '-RM':
                            name = name.split('.')[1].split(':')[0]
                        else:
                            name = name[:-3]
                        stock = Stocks.objects.get(name=name)
                        price = df.iloc[:, [7]][df.iloc[:, [7]].columns[0]][0]
                        last_price = HandlingFunctions.get_last_price(stock)
                        timer = HandlingFunctions.get_timer(stock.pk)
                        is_frozen = HandlingFunctions.get_pause(stock.pk)
                        if Quotes.objects.filter(price=price, stock=stock, line=i):
                            is_exist = True
                        if not Tendencies.settings_check(stock, user, AMOUNT, last_price, timer) and not is_exist:
                            HandlingFunctions.generate_orders(user, stock, price, AMOUNT, i)
                        else:
                            settings_interruption = 1
                    if not is_exist:
                        time.sleep(timer)
                else:
                    break
        MainCycle.begin(AMOUNT, user)

    except KeyboardInterrupt:
        logging.info('Бот остановлен пользователем')


if __name__ == "__main__":
    price_bot()
