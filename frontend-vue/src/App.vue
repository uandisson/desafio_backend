

<template>
    <div class="container">
        <p><router-link :to="{ name: 'all_customers' }" class="btn btn-primary">Home</router-link>
        <router-link :to="{ name: 'simulation' }" class="btn btn-primary">Simulation</router-link></p>
        <img src="src/assets/imgs/logo.jpg">

        <div id="page">
            <transition name="fade">
                <router-view></router-view>
            </transition>
        </div>
    </div>
</template>
<!-- lang="sass"
<style>

    .fade-enter-active, .fade-leave-active {
      transition: opacity .5s
    }
    .fade-enter, .fade-leave-active {
      opacity: 0
    }
</style>
 -->
<script>

    export default {
        //name: "app",
        data(){
            return{

            }
        }
    }    
</script>