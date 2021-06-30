<template>
  <v-row>
    <v-col cols="1" v-for="(stock) in stocks" :key="stock.id">
      <v-card v-bind:disabled="!stock.is_active" elevation="0" outlined @click="$router.push({ name: 'Stoks', params:{id:stock.id }})">
        <v-row no-gutters class="text-center">
          <v-col cols="12">
            <v-avatar color="red">
              <span class="white--text text-h5">{{stock.name[0] + stock.name[1]}}</span>
            </v-avatar>
          </v-col>
          <v-col cols="12">
            {{stock.name}}
          </v-col>
          <v-col cols="12">
            {{stock.description}}
          </v-col>
          <v-col cols="12">
            {{ stock.price.toFixed(2) }}&#x20AE;
          </v-col>
        </v-row>

      </v-card>
    </v-col>
  </v-row>
</template>

<script>
  import {
    getAPI
  } from '@/axios-api'

  export default {
    name: 'App',

    data: () => ({
      stocks: [],
      stocksInterval: undefined,
    }),

    methods: {
      getStocks() {
        getAPI.get('api/v1/stocks/', {
            headers: {
              Authorization: `Bearer ${this.$store.getters.accessToken}`
            }
          })
          .then(response => {
            this.stocks = response.data
          })
          .catch(err => {
            console.log(err)
            clearInterval(this.stocksInterval)
          })
      }
    },
    mounted() {
      this.getStocks()
      this.stocksInterval = setInterval(function () {
        this.getStocks()
      }.bind(this), 5000)
    },

    destroyed() {
      clearInterval(this.stocksInterval)
    }
  }

</script>
