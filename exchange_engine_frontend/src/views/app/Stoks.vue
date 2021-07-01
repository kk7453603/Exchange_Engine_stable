<template>
    <v-row>
        <v-col cols="12">
            <span @click="$router.push({ name: 'App'})">
                <v-icon>mdi-arrow-left</v-icon> Назад
            </span>
        </v-col>
        <v-col>
            <h1 class="text-h4 text-xl-h3 text-truncate">{{stock.name}}</h1>
        </v-col>
        <v-col>
            <div class="d-flex flex-column text-right">
                <p class="text-body-1 ma-0 text-no-wrap">{{stock.price.toFixed(2)}}₮</p>
                <!--<p class="text-body-1 ma-0 green--text darken-1 text-no-wrap">
                    <v-icon x-small color="green">mdi-arrow-up</v-icon> 1 084,12 ₮ (1,42 %)
                </p>-->
            </div>
        </v-col>
        <v-col cols="12">
            <v-btn-toggle style="width: 100%;" v-model="text" mandatory>
                <v-row>
                    <v-col>
                        <v-btn outlined block elevation="0">
                            1m
                        </v-btn>
                    </v-col>
                    <v-col>
                        <v-btn outlined block elevation="0">
                            5m
                        </v-btn>
                    </v-col>
                    <v-col>
                        <v-btn outlined block elevation="0">
                            15m
                        </v-btn>
                    </v-col>
                    <v-col>
                        <v-btn outlined block elevation="0">
                            30m
                        </v-btn>
                    </v-col>
                    <v-col>
                        <v-btn outlined block elevation="0">
                            60m
                        </v-btn>
                    </v-col>
                </v-row>
            </v-btn-toggle>
        </v-col>
        <v-col cols="12">
            <apexchart height="450" type="candlestick" :options="options" :series="series"></apexchart>
        </v-col>
        <v-col cols="12">
            <h1 v-if="stocks_portfolio!=undefined">В портфеле</h1>
            <v-row class="align-center justify-end">
                <v-col v-if="stocks_portfolio!=undefined" cols="12" sm="6">
                    <v-card outlined elevation="0" class="pa-2 mt-8 mb-8">
                        <v-card-text class="pb-0">
                            <v-row class="flex-sm-row">
                                <v-col class="text-center">
                                    <p class="text-h5">{{stocks_portfolio.count}} {{stocks_portfolio.count == 1 ? 'акция' : 'акций'}}</p>
                                    <p class="text-subtitle-1 text-no-wrap">{{stocks_portfolio.stock.price.toFixed(2)}}₮ → {{stocks_portfolio.aver_price.toFixed(2)}}₮ </p>
                                </v-col>
                            </v-row>
                        </v-card-text>
                    </v-card>
                </v-col>
                <v-col v-if="stocks_portfolio!=undefined" cols="6" sm="3">
                    <sellStock :stocks_portfolio="stocks_portfolio"/>
                </v-col>
                <v-col v-bind:cols="[stocks_portfolio!=undefined ? 6 : 12]" sm="3">
                    <buyStock :stock="stock"/>
                </v-col>
            </v-row>
        </v-col>

    </v-row>
</template>

<script>
    import {
        getAPI
    } from '@/axios-api'

    export default {
        components: {
            sellStock: () => import('@/components/app/stocks/sell.vue'),
            buyStock: () => import('@/components/app/stocks/buy.vue'),
        },
        computed: {
            stocks_portfolio(){
                let p = this.$store.getters.portfolio
                if ((p.length == 0)){
                    return undefined
                }
                return p.find(item => item.stock.id == this.$route.params.id);
            }
        },
        methods: {
            getStocks() {   
                getAPI.get('api/v1/stocks/' + this.$route.params.id, {
                        headers: {
                            Authorization: `Bearer ${this.$store.getters.accessToken}`
                        }
                    })
                    .then(response => {
                        this.stock = response.data
                    })
                    .catch(err => {
                        console.log(err)
                        clearInterval(this.stocksInterval)
                    })

            },
            getCandles() {
                if(this.$route.params.id!=undefined){
                    getAPI.get('/api/v1/candles/' + this.$route.params.id + '/' + (this
                        .selectedCandlesType + 1))
                    .then(response => {
                        let data = response.data.map(function (candle) {
                            return [Date.parse(candle.date), [candle.open, candle.high, candle.low, candle
                                .close
                            ].map((price) => (price.toFixed(2)))]
                        })

                        this.candlesInterval = setInterval(function () {
                            this.getCandles()
                        }.bind(this), 60000)

                        this.series = [{
                            data: data
                        }]
                    })
                    .catch(err => {
                        console.log(err)
                    })
                }
            }
        },
        watch: {
            selectedCandlesType: function () {
                this.getCandles()
            }
        },
        created() {
            this.getStocks()
            this.getCandles()
        },
        data: () => ({
            selectedCandlesType: 0,
            stock: {},
            candlesInterval: undefined,
            model: '',
            dialog2: false,
            text: '',
            options: {
                chart: {
                    id: 'main-chart',
                    locales: [{
                        "name": "ru",
                        "options": {
                            "months": ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль",
                                "Август", "Сентябрь",
                                "Октябрь", "Ноябрь", "Декабрь"
                            ],
                            "shortMonths": ["Янв", "Фев", "Мар", "Апр", "Май", "Июн", "Июл", "Авг",
                                "Сен", "Окт", "Ноя",
                                "Дек"
                            ],
                            "days": ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг",
                                "Пятница", "Суббота"
                            ],
                            "shortDays": ["Вс", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб"],
                            "toolbar": {
                                "exportToSVG": "Скачать SVG",
                                "exportToPNG": "Скачать PNG",
                                "menu": "Меню",
                                "selection": "Зона",
                                "selectionZoom": "Зона увелечения",
                                "zoomIn": "Увеличить",
                                "zoomOut": "Уменьшить",
                                "pan": "Переместить",
                                "reset": "Домой"
                            }
                        }
                    }],
                    defaultLocale: "ru",
                    animations: {
                        enabled: true,
                        easing: 'easeinout',
                        speed: 300,
                        animateGradually: {
                            enabled: true,
                            delay: 100
                        },
                        dynamicAnimation: {
                            enabled: true,
                            speed: 100
                        }
                    },
                    toolbar: {
                        show: true,
                        offsetX: 0,
                        offsetY: 0,
                        tools: {
                            download: true,
                            selection: true,
                            zoom: true,
                            zoomin: true,
                            zoomout: true,
                            pan: true,
                            reset: true | '<img src="/static/icons/reset.png" width="20">',
                            customIcons: []
                        },
                    }
                },
                xaxis: {
                    type: 'datetime'
                },
                yaxis: {
                    tooltip: {
                        enabled: true
                    }
                }
            },
            series: [{
                data: []
            }]
        })
    }

</script>

<style>

</style>
