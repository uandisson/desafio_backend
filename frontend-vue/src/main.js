import Vue from 'vue'

import VueRouter from 'vue-router'
Vue.use(VueRouter)

import VueResource from 'vue-resource';
Vue.use(VueResource);

import App from './App.vue'

const AllCustumers = require('./assets/js/components/customer/all-customers.vue');
const EditCustomer = require('./assets/js/components/customer/edit-customer.vue');
const DeleteCustomer = require('./assets/js/components/customer/delete-customer.vue');

const Simulation = require('./assets/js/components/simulation.vue');

const routes = [
    {
        name: 'all_customers',
        path: '/',
        component: AllCustumers
    },
    {
        name: 'edit_customer',
        path: '/customers/edit/:cpf',
        component: EditCustomer
    },
    {
        name: 'delete_customer',
        path: '/customers/delete/:cpf',
        component: DeleteCustomer
    },
    {
        name: 'simulation',
        path: '/simulation',
        component: Simulation
    }
];

var router = new VueRouter({ routes: routes, mode: 'history' });
new Vue(Vue.util.extend({ router }, App)).$mount('#app');