import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import toast from './plugins/toast'

Vue.config.productionTip = false

new Vue({
  router,
  vuetify,
  toast, 
  render: h => h(App)
}).$mount('#app')
