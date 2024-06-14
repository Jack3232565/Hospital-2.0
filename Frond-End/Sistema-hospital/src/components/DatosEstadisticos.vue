<template>
    <h1>Datos Estadisiticos</h1>

    <div class="xl bg-blue-300 text-white md text-center text-uppercase p-2 ">
        <h1>Contenido</h1>
        <div class=" columns-3 ">
          <div class="xl bg-green-700 text-white text-center p-5 rounded-md">
            <span class=" box-decoration-slice bg-gradient-to-r  italic hover:not-italic from-indigo-600  to-purple-500 text-white px-2 ... ">
              Bienvenido
              <br>
              Hospital
            </span>
    
          </div>
    
          <div class="xl bg-blue-700 text-white text-center p-5">
            Hospital Pruvilege Care
            <br>
          </div>
          
          <div class="xl bg-red-700 text-white text-center p-5">Modulos de Atención</div>
        
        </div>
    
       
      </div>
    
      <h1>Sedebe considerar los siguiente puentos:</h1>
      <ul>
        <li>botones</li>
        <li>iconos</li>
        <li>Colores de fuente</li>
        <li>Titulos</li>
        <li>Color de fondo</li>
        <li>Tipo de Letra</li>
      </ul>
    
      
      <div>
        <!-- Modal toggle -->
        <button @click="toggleModal"
                class="block text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                type="button">
          Editar
        </button>
        <button @click="toggleModal"
                class="block text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                type="button">
          Eliminar
        </button>
    
        <!-- Main modal -->
        <div v-if="modalVisible"
             id="static-modal"
             data-modal-backdrop="static"
             tabindex="-1"
             aria-hidden="true"
             class="fixed top-0 right-0 left-0 z-50 flex justify-center items-center w-full h-full bg-black bg-opacity-50 overflow-y-auto">
          <div class="relative p-4 w-full max-w-2xl max-h-full">
            <!-- Modal content -->
            <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
              <!-- Modal header -->
              <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
                <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
                  Static modal
                </h3>
                <button @click="toggleModal"
                        type="button"
                        class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
                        data-modal-hide="static-modal">
                  <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                          d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                  </svg>
                  <span class="sr-only">Close modal</span>
                </button>
              </div>
              
              <!-- Modal body -->
              <div class="p-4 md:p-5 space-y-4">
                <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
                  With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply.
                </p>
                <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
                  The European Union’s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.
                </p>
              </div>
              <!-- Modal footer -->
              <div class="flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600">
                <button @click="acceptModal"
                        type="button"
                        class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                  I accept
                </button>
                <button @click="declineModal"
                        type="button"
                        class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">
                  Decline
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>


    
</template>

<script>
export default {
  data() {
    return {
      modalVisible: false
    };
  },
  methods: {
    toggleModal() {
      this.modalVisible = !this.modalVisible;
    },
    acceptModal() {
      // Handle logic for accepting modal
      this.modalVisible = false; // Close modal after accepting
    },
    declineModal() {
      // Handle logic for declining modal
      this.modalVisible = false; // Close modal after declining
    }
  }
};
</script>

<style scoped>
/* Aquí puedes agregar estilos específicos para tu modal si es necesario */
</style>