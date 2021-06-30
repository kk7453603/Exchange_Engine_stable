export default [{
  path: '/app',
  component: () => import('../layouts/App.vue'),
  meta: {
    requiresLogin: false
  },
  children: [{
      path: '',
      name: 'App',
      component: () => import('../views/app/children/Main.vue')
    },
    {
      path: 'profile',
      name: 'Profile',
      component: () => import('../views/app/children/Profile.vue')
    },
    {
      path: 'portfolio',
      name: 'Portfolio',
      component: () => import('../views/app/children/Portfolio.vue')
    },
    {
        path: 'stocks/:id',
        name: 'Stocks',
        component: () => import('../views/app/Stoks.vue')
    },
    {
      path: 'orders',
      name: 'Orders',
      component: () => import('../views/app/children/Orders.vue')
    }
  ]
}]
