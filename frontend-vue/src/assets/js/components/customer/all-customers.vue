<template>
    <div id="all-customers">
        <h1><img src="src/assets/imgs/users.png" alt="Negativado" border=3 height=32px width=32px>All Customers</h1>
        
        <p><router-link :to="{ name: 'create_customer' }" class="btn btn-primary">Create Customer</router-link></p>

        <div class="form-group">
            <input type="text" name="search" v-model="customerSearch" placeholder="Search customers" class="form-control" v-on:keyup="searchCustomers">
        </div>

        <table class="table table-hover">
            <thead>
            <tr>
                <td>Nome</td>
                <td>CPF</td>
                <td>Telefone</td>
                <td>Score</td>  
                <td>Status</td>                
            </tr>
            </thead>

            <tbody>
                <tr v-for="customer in customers">
                    <td>{{ customer.nome }}</td>
                    <td>{{ customer.cpf }}</td>
                    <td>{{ customer.celular }}</td>
                    <td>{{ customer.score }}</td>
                    <td v-if="customer.negativado">
                        <img src="src/assets/imgs/negativado.png" alt="Negativado" border=3 height=27px width=27px>
                    </td>
                    <td v-else-if="customer.score > 500">
                        <img src="src/assets/imgs/socre_alto.png" alt="" border=3 height=27px width=27px>
                    </td>
                    <td v-else-if="customer.score <= 500">
                        <img src="src/assets/imgs/socre_baixo.png" alt="" border=3 height=27px width=27px>
                    </td>
                    <td>
                        <router-link :to="{name: 'edit_customer', params: { cpf: customer.cpf }}" class="btn btn-primary">Edit</router-link>
                        <router-link :to="{name: 'delete_customer', params: { cpf: customer.cpf }}" class="btn btn-danger">Delete</router-link>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    import { API_URL } from '../util/URL_API';

    export default{
        data(){
            return{
                customers: [],
                originalCustomers: [],
                customerSearch: ''
            }
        },

        created: function()
        {
            this.fetchCustomerData();
        },

        methods: {
            fetchCustomerData: function()
            {
                this.$http.get(API_URL+'/customers').then((response) => {
                    console.log(response)
                    this.customers = response.body;
                    this.originalCustomers = this.customers;
                }, (response) => {

                });
            },

            searchCustomers: function()
            {
                if(this.customerSearch == '')
                {
                    this.customers = this.originalCustomers;
                    return;
                }

                var searchedCustomers = [];
                for(var i = 0; i < this.originalCustomers.length; i++)
                {
                    var customerName = this.originalCustomers[i]['nome'].toLowerCase();
                    if(customerName.indexOf(this.customerSearch.toLowerCase()) >= 0)
                    {
                        searchedCustomers.push(this.originalCustomers[i]);
                    }
                }

                this.customers = searchedCustomers;
            }
        }
    }
</script>
