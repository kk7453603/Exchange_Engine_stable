export default [{
  path: '/auth',
  component: () => import('../views/auth/View.vue'),
  children: [{
      path: 'login',
      name: 'Login',
      component: () => import('../views/auth/children/Login.vue'),
    },
    {
      path: 'reg',
      name: 'Registration',
      component: () => import('../views/auth/children/Reg.vue'),
    },
    {
      path: 'logout',
      name: 'Logout',
      component: () => import('../views/auth/children/Logout.vue')
    }
  ]
}]
