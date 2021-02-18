<template>
    <!-- The Modal -->
     <div class="modal" id="myModal" style="display: block;">
       <div class="modal-dialog">
         <div class="modal-content">
           <!-- Modal Header -->
           <div class="modal-header">
             <h4 class="modal-title">Simulation</h4>
             <button type="button" class="close" @click="$emit('close')" data-dismiss="modal">×</button>
           </div>
           <!-- Modal body -->
           <div class="modal-body">
             <slot></slot>
           </div>
           <!-- Modal footer -->
           <div class="modal-footer">
             <button type="button" @click="$emit('close')" class="btn btn-danger" data-dismiss="modal">Fechar</button>
           </div>
         </div>
       </div>
     </div>
</template>
<script>
    export default{
        data(){
            return{
            }
        },
        props: ['modal']
    }
</script>