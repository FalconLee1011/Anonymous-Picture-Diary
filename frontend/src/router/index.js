import Vue from 'vue'
import VueRouter from 'vue-router'
import create from '../components/create'
import home from '../components/home'

import get from '../components/get'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: home
  },
  {
    path: '/upload',
    name: 'create',
    component: create
  },
  {
    path: '/get',
    name: 'get',
    component: get
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
