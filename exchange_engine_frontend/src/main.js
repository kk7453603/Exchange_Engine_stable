import Vue from 'vue'
import App from './App.vue'
import VueMeta from 'vue-meta'
import axios from 'axios'
import VueAxios from 'vue-axios'
import vuetify from './plugins/vuetify';
import router from './router'
import store from './store'
import IdleVue from 'idle-vue'
import './plugins/base'

const eventsHub = new Vue()

Vue.use(IdleVue, {
  eventEmitter: eventsHub,
  idleTime: 1000,
  keepTracking: true
})
Vue.use(VueMeta)
Vue.use(VueAxios, axios)

Vue.config.productionTip = false

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresLogin)) {
    if (!store.getters.loggedIn) {
      next({ name: 'Login' })
    } else {
      next()
    }
  } else {
    next()
  }
})

new Vue({
  vuetify,
  router,
  store,
  beforeCreate() {
    this.$store.commit('initialiseStore')
  },
  render: h => h(App)
}).$mount('#app')
