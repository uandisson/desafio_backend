<template>
    <div id="delete-customer">
        <h1>Delete Customer {{ customer.nome }}</h1>

        <p><router-link :to="{ nome: 'all_customers' }">Return to customers</router-link></p>

        <notification v-bind:notifications="notifications"></notification>

        <form v-on:submit.prevent="deleteCustomer">
            <p><button class="btn btn-danger">Delete Customer</button></p>
        </form>
    </div>
</template>

<script>
    import Notification from '../notifications.vue';

    export default{
        data(){
            return{
                customer:{},
                notifications:[]
            }
        },

        created: function(){
            this.getCustomer();
        },

        methods: {
            getCustomer: function()
            {
                this.$http.get('http://localhost:3000/api/v1/customer/' + this.$route.params.id).then((response) => {
                    this.customer = response.body;
                }, (response) => {

                });
            },

            delete: function()
            {
                this.$http.delete('http://localhost:3000/api/v1/customer/delete/' + this.$route.params.id, this.customer, {
                    headers : {
                        'Content-Type' : 'application/json'
                    }
                }).then((response) => {
                    this.$router.push({name: 'all_customers'})
                }, (response) => {
                    this.notifications.push({
                        type: 'danger',
                        message: 'Customer could not deleted'
                    });
                });
            }
        },

        components: {
            'notification' : Notification
        }
    }
</script>
