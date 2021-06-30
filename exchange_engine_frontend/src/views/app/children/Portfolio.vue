<template>
  <v-row class="flex-column-reverse flex-md-row">
    <v-col cols="12" md="8">
      <v-list two-line class="transparent">
        <v-list-item-group color="">
          <v-subheader inset class="text-h6"> Акции </v-subheader>
          <v-list-item v-for="(security) in portfolio" :key="security.stock.id"
            @click="$router.push({ name: 'Stocks', params:{id:security.stock.id }})">
            <v-list-item-avatar>
              <v-icon class="grey lighten-1" dark> </v-icon>
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title v-text="security.stock.name"></v-list-item-title>

              <v-list-item-subtitle v-text="security.count + ' шт.'"></v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-action>
              <p class="text-overline ma-0">{{security.stock.price.toFixed(2)}}₮</p>
              <p class="text-caption ma-0 green--text darken-1">
                <v-icon x-small color="green">mdi-arrow-up</v-icon> {{(security.stock.price - security.aver_price).toFixed(2)}}₮ ({{ ((security.stock.price - security.aver_price) / security.stock.price * 100).toFixed(2) }}%)
              </p>
            </v-list-item-action>
          </v-list-item>
          <v-divider></v-divider>
        </v-list-item-group>
      </v-list>
    </v-col>
    <v-col cols="12" md="4">
      <v-card outlined elevation="0" class="pa-2 mb-8 rounded-xl">
        <v-card-title class="text-h6 ">Стоимость портвеля</v-card-title>
        <v-card-text class="pt-2 pb-0">
          <v-row class="justify-space-between align-center">
            <v-col cols="auto">
              <h1>{{summ_potfolio.toFixed(2)}}₮</h1>
            </v-col>
            <v-col>
              <p class="text-right text-subtitle-1 ma-0 green--text darken-1" style="white-space: nowrap;">
                <v-icon x-small color="green">mdi-arrow-up</v-icon> 1 084,12 ₮ (1,42 %)
              </p>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
      <v-card outlined elevation="0" class="pa-2 mb-8 rounded-xl">
        <v-card-title class="text-h6">Баланс</v-card-title>
        <v-card-text class="pt-2 pb-0">
          <v-row class="justify-space-between align-center">
            <v-col cols="auto">
              <h1>{{profile.balance.toFixed(2)}}₮</h1>
            </v-col>
            <v-col class="d-flex justify-space-around">
              <div class="d-flex flex-column justify-center align-center">
                <v-btn class="mx-2" fab dark small>
                  <v-icon dark>
                    mdi-plus
                  </v-icon>
                </v-btn>
                <p class="caption mt-1">Пополнить</p>
              </div>
              <div class="d-flex flex-column justify-center align-center">
                <v-btn class="mx-2" fab dark small>
                  <v-icon dark>
                    mdi-clipboard-text
                  </v-icon>
                </v-btn>
                <p class="caption mt-1">Операции</p>
              </div>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    name: 'App',

    computed: {
      portfolio() {
        console.log(this.$store.getters.portfolio)
        return this.$store.getters.portfolio
      },
      profile() {
        return this.$store.getters.profile
      },
      summ_potfolio(){
        let summa = 0
        for(let item of this.$store.getters.portfolio){
          summa+=item.stock.price
        }
        return summa
      }
    },

    methods: {
      sumSecurities(securities) {
        let sum = 0

        for (let key in securities) {
          sum += securities[key].price
        }

        return sum.toFixed(2)
      }
    },

    data: () => ({
      portfolioInterval: undefined,
    })
  }

</script>


<style>

</style>
