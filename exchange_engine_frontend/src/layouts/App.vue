<template>
    <v-app>
        <AppBar />
        <v-main>
            <v-container>
                <v-fade-transition mode="out-in">
                    <router-view></router-view>
                </v-fade-transition>
            </v-container>
        </v-main>
        <BaseSnackbar dark />
    </v-app>
</template>

<script>
export default {
    name: 'AppView',
    components: {
			AppBar: () => import('@/components/app/AppBar')
		},

    props: {
      id: {
        type: String,
        default: 'view',
      },
    },
    data: () => ({
      userInfoInterval: undefined
    }),
    methods: {
      showSnackbar () {
        this.$store.commit({
          type: 'showSnackbar',
          text: 'Hello'
        })
      },
      getUserInfo () {
        this.$store.dispatch('getProfile')
        this.$store.dispatch('getPortfolio')
      }
    },
    beforeCreate () {
      this.$store.dispatch('initialiseToken')
    },
    mounted() {
      this.getUserInfo()
      this.userInfoInterval = setInterval(function() {
        this.getUserInfo()
      }.bind(this), 1000)
    },
    destroyed() {
      clearInterval(this.userInfoInterval)
    }
}
</script>