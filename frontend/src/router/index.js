import Vue from 'vue'
import VueRouter from 'vue-router'
import create from '../components/create'
import home from '../components/home'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: home
  },
  {
    path: '/create',
    name: 'create',
    component: create
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
