<template>
    <div id="simulation">
        <h1>Simulation with Customer</h1>

        <notification v-bind:notifications="notifications"></notification>
       
        <form v-on:submit.prevent="checkCustomer">
            <div class="form-group">
                <label name="customer_cpf">CPF</label>
                <the-mask class="form-control" id="customer_cpf" required v-model="customer.cpf" :mask="['###.###.###-##']" />
            </div>

            <div class="form-group">
                <label name="customer_phone_number">Celular</label>
                <the-mask class="form-control" id="customer_phone_number" required v-model="customer.phone_number" :mask="['(##) ####-####', '(##) #####-####']" />
            </div>

            <div class="form-group">
                <button class="btn btn-primary">Login</button>
            </div>
        </form>
        
        <h1>Simulation without Customer</h1>
        
        <div class="form-group">
            <button @click="showModel = true" class="btn btn-primary">Simulate</button>
        </div>
        
         <modal v-if="showModel" @close="showModel = false">
            <notification v-bind:notifications="notificationsModal"></notification>
            <form v-on:submit.prevent="getSimulation">
                <div class="form-group">
                    <label name="loan_value">Valor Empréstimo</label>
                    <input type="text" class="form-control" v-model="loan.loan_value" id="loan_value" required >
                </div>

                <div class="form-group">
                    <label name="loan_installments">Número de Parcelas</label>
                    <select class="form-control" id="loan_installments" name="installments" v-model="loan.installments">
                        <option value="6">6x</option>
                        <option value="12">12x</option>
                        <option value="18">18x</option>
                        <option value="24">24x</option>
                        <option value="36">36x</option>					
                    </select>
                </div>

                <div class="form-group">
                    <button class="btn btn-primary">Simular</button>
                </div>
            </form>
         </modal>
    </div>
</template>



<script>
    import Notification from './notifications.vue';
    import modal from "./modal-loan.vue";
    import { API_URL } from './util/URL_API';

    export default{
        data(){
            return{
                customer:{},
                loan:{},
                notifications:[],
                notificationsModal:[],
                modal:[],
                showModel:false
                
            }
        },

        methods: {
            checkCustomer: function()
            {
                // Validation
                var cpf = parseInt(this.customer.cpf);
                if(isNaN(cpf))
                {
                    this.notifications.push({
                        type: 'danger',
                        message: 'CPF must be a number'
                    });
                    return false;
                } else {
                    this.customer.cpf = this.customer.cpf;
                }

                var phone_number = parseInt(this.customer.phone_number);
                if(isNaN(phone_number))
                {
                    this.notifications.push({
                        type: 'danger',
                        message: 'Phone number must be a number'
                    });
                    return false;
                } else {
                    this.customer.phone_number = this.customer.phone_number;
                }
                
                var jsonData = '{"cpf": "' + this.customer.cpf + '", "phone_number": "'+ this.customer.phone_number +'"}'

                this.$http.post(API_URL + '/login', this.customer, {
                    headers : {
                        'Content-Type' : 'application/json'
                    }, jsonData
                }).then((response) => {
                    console.log(response)
                    console.log(response.body.status)
                    if(response.body.status == true){
                        this.notifications.push({
                            type: 'success',
                            message: 'All right, find customer!'
                        });
                        this.showModel = true;
                    }else{
                        this.notifications.push({
                            type: 'danger',
                            message: 'Ohhh no, customer not found!'
                        });
                    }
                    
                }, (response) => {
                    this.notifications.push({
                        type: 'error',
                        message: 'Ohhh no, error!'
                    });
                });
            },
            getSimulation: function()
            {
                // Validation
                var loan_value = parseFloat(this.loan.loan_value);
                if(isNaN(loan_value))
                {
                    this.notifications.push({
                        type: 'danger',
                        message: 'Loan value must be a number'
                    });
                    return false;
                } else {
                    this.loan.loan_value = this.loan.loan_value;
                }
                
                var jsonData = '{"cpf": "' + this.customer.cpf + '", "phone_number": "'+ this.customer.phone_number + '", "loan_value": "' + this.loan.loan_value + '", "installments": "' + this.loan.installments + '"}'
              
                this.$http.post(API_URL + '/loan', jsonData, {
                    headers : {
                        'Content-Type' : 'application/json'
                    }
                }).then((response) => {
                    this.showModel = true;
                    var tax = parseFloat(response.body.data);
                                            
                    console.log(this.loan.loan_value);
                    console.log(this.loan.installments);
                    console.log(tax);
			 	    this.simulation(this.loan.loan_value, this.loan.installments, tax);
                    
                }, (response) => {
                    this.notificationsModal.push({
                        type: 'error',
                        message: 'Ohhh no, error!'
                    });
                });
            },
            simulation: function(loan_value, installments, tax) 
            {
                var jsonData = '{"loan_value": "' + loan_value + '", "installments": "'+ installments + '", "tax": "' + tax + '"}'
                
                this.$http.post(API_URL + '/simulation', jsonData, {
                    headers : {
                        'Content-Type' : 'application/json'
                    }
                }).then((response) => {
                    console.log(response)
                    console.log(response.body.status)
                    
                        this.notificationsModal.push({
                            type: 'success',
                            message: response.body.message
                        });
                       
                }, (response) => {
                    this.notificationsModal.push({
                        type: 'error',
                        message: 'Ohhh no, error!'
                    });
                });

            }
        },

        components: {
            'notification' : Notification,
            'modal': modal
        }
    }
</script>
