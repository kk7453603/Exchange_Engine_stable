import Vue from 'vue'
import VueRouter from 'vue-router'
import RoutesApp from './routesApp'
import RoutesAuth from './routesAuth'

Vue.use(VueRouter)

const routes = [
  ...RoutesApp,
  ...RoutesAuth,
  {
    path: '/',
    component: () => import('../components/home/layouts/Index.vue'),
    children: [{
      path: '',
      name: 'Home',
      component: () => import('../views/home/children/Index.vue'),
    }]
  },
  {
    path: '/test',
    component: () => import('../views/test/Graph.vue'),
    children: [{
        path: 'hexagon-ava',
        name: 'Hexagon',
        component: () => import('../views/test/Hexagon.vue')
      },
      {
        path: 'graph',
        name: 'Graph',
        component: () => import('../views/test/Graph.vue')
      }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
