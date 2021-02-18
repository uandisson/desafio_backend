<template>
    <div id="update-customer">
        <h1>Update Customer</h1>

        <p><router-link :to="{ name: 'all_customer' }">Return to customers</router-link></p>

        <notification v-bind:notifications="notifications"></notification>

        <form v-on:submit.prevent="editCustomer">
            <div class="form-group">
                <label name="customer_cpf">CPF</label>
                <input type="text" class="form-control" disabled v-model="customer.cpf" id="customer_cpf">
            </div>

            <div class="form-group">
                <label name="customer_name">Nome</label>
                <input type="text" class="form-control" v-model="customer.nome" id="customer_name" required>
            </div>

            <div class="form-group">
                <label name="customer_negative">Negativado</label>
                <input type="text" class="form-control" v-model="customer.negativado" id="customer_negative" required>
            </div>

            <div class="form-group">
                <button class="btn btn-primary">Update</button>
            </div>
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
                this.$http.get('http://localhost:3000/api/customer/' + this.$route.params.id).then((response) => {
                    this.customer = response.body;
                }, (response) => {

                });
            },

            editCustomer: function()
            {
                // Validation
                var price = parseFloat(this.customer.price);
                if(isNaN(price))
                {
                    this.notifications.push({
                        type: 'danger',
                        message: 'Price must be a number'
                    });
                    return false;
                }

                this.$http.patch('http://localhost:3000/api/customer/edit/' + this.$route.params.id, this.customer, {
                    headers : {
                        'Content-Type' : 'application/json'
                    }
                }).then((response) => {
                    this.notifications.push({
                        type: 'success',
                        message: 'Customer updated successfully'
                    });
                }, (response) => {
                    this.notifications.push({
                        type: 'error',
                        message: 'Customer not updated'
                    });
                });
            }
        },

        components: {
            'notification' : Notification
        }
    }
</script>
