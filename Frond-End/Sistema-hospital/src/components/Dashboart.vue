<template>
  <div class="flex h-screen bg-gray-100">
    <!-- Sidebar -->
    <div class="hidden md:flex flex-col w-64 bg-gray-800">
      <div class="flex items-center justify-center h-16 bg-gray-900">
        <img src="../assets/img/Logo propuesto Hospital 1.png" alt="Descripción de la imagen" width="170" height="100" class="mr-2">
      </div>
      <div class="flex flex-col flex-1 overflow-y-auto">
        <nav class="flex-1 px-2 py-4 bg-gray-800">
          <!-- Dirección General -->
          <div class="menu-item">
            <a href="#" @click.prevent="toggleMenu('general')" class="flex items-center px-4 py-2 text-gray-100 hover:bg-gray-700">
              <img src="../assets/img/Direccion General.png" alt="Descripción de la imagen" width="35" height="40" class="mr-2">
              Dirección General
            </a>
            <ul v-show="menus.general" class="submenu ml-8">
              
              <RouterLink to="/aprobacionSM">
                <li>
                    <a href="#" class="flex items-center px-4 py-2 text-gray-100 hover:bg-gray-700">
                      <img src="../assets/img/Aprobacion.webp" alt="Descripción de la imagen" width="25" height="40" class="mr-2">
                      Aprobación S. M.
                    </a>
                </li>
              </RouterLink>
              
              <RouterLink to="/estrucuturaOr">
                <li>
                  <a href="#" class="flex items-center px-4 py-2 text-gray-100 hover:bg-gray-700">
                    <img src="../assets/img/Organizacion.webp" alt="Descripción de la imagen" width="25" height="40" class="mr-2">
                    Estructura O. H.
                  </a>
                </li>
              </RouterLink>

              <RouterLink to="/estadisticas">
                <li>
                  <a href="#" class="flex items-center px-4 py-2 text-gray-100 hover:bg-gray-700">
                    <img src="../assets/img/Graficos.webp" alt="Descripción de la imagen" width="25" height="40" class="mr-2">
                    Datos Estadísticos
                  </a>
                </li>
              </RouterLink>

              <RouterLink to="/bitacora">
                <li>
                  <a href="#" class="flex items-center px-4 py-2 text-gray-100 hover:bg-gray-700">
                    <img src="../assets/img/Bitacora.webp" alt="Descripción de la imagen" width="25" height="40" class="mr-2">
                    Bitácora
                  </a>
                </li>
              </RouterLink>

            </ul>
          </div>
          
          <!-- Recursos Humanos -->
          <div class="menu-item">
            <a href="#" @click.prevent="toggleMenu('hr')" class="flex items-center px-4 py-2 text-gray-100 hover:bg-gray-700">
              <img src="../assets/img/Recursos Humanos.png" alt="Descripción de la imagen" width="35" height="40" class="mr-2">
              Recursos Humanos
            </a>
            <ul v-show="menus.hr" class="submenu ml-8">
              <RouterLink to="/personas">
                <li><a href="#" class="block px-4 py-2 text-gray-100 hover:bg-gray-700">Personas</a></li>
              </RouterLink>
              <li><a href="#" class="block px-4 py-2 text-gray-100 hover:bg-gray-700">Personal Medico</a></li>
              <li><a href="#" class="block px-4 py-2 text-gray-100 hover:bg-gray-700">Horarios</a></li>
              <li><a href="#" class="block px-4 py-2 text-gray-100 hover:bg-gray-700">Puestos</a></li>
            </ul>
          </div>

          <!-- Registros Médico -->
          <div class="menu-item">
            <a href="#" @click.prevent="toggleMenu('rmedicos')" class="flex items-center px-4 py-2 text-gray-100 hover:bg-gray-700">
              <img src="../assets/img/Registros Medicos.webp" alt="Descripción de la imagen" width="35" height="50" class="mr-2">
              Registros Médico
            </a>
            <ul v-show="menus.rmedicos" class="submenu ml-8">
              <li><a href="#" class="block px-4 py-2 text-gray-100 hover:bg-gray-700">Citas</a></li>
              <li><a href="#" class="block px-4 py-2 text-gray-100 hover:bg-gray-700">Expediente Medico</a></li>
              <li><a href="#" class="block px-4 py-2 text-gray-100 hover:bg-gray-700">Receta Médica</a></li>
            </ul>
          </div>

          <!-- Pediatria -->
          <div class="menu-item">
            <a href="#" @click.prevent="toggleMenu('pediatria')" class="flex items-center px-4 py-2 text-gray-100 hover:bg-gray-700">
              <img src="../assets/img/Pediatria.webp" alt="Descripción de la imagen" width="35" height="50" class="mr-2">
              Pediatria
            </a>
            <ul v-show="menus.pediatria" class="submenu ml-8">
              <li><a href="#" class="block px-4 py-2 text-gray-100 hover:bg-gray-700">Nacimientos</a></li>
              <li><a href="#" class="block px-4 py-2 text-gray-100 hover:bg-gray-700">Desarrollo Infantil</a></li>
            </ul>
          </div>

          <!-- Farmacia -->
          <div class="menu-item">
            <a href="#" @click.prevent="toggleMenu('farmacia')" class="flex items-center px-4 py-2 text-gray-100 hover:bg-gray-700">
              <img src="../assets/img/Farmacia.webp" alt="Descripción de la imagen" width="35" height="50" class="mr-2">
              Farmacia
            </a>
            <ul v-show="menus.farmacia" class="submenu ml-8">
              <li><a href="#" class="block px-4 py-2 text-gray-100 hover:bg-gray-700">Consumibles</a></li>
              <li><a href="#" class="block px-4 py-2 text-gray-100 hover:bg-gray-700">Medicamentos</a></li>
              <li><a href="#" class="block px-4 py-2 text-gray-100 hover:bg-gray-700">Lote Medicamento</a></li>
              <li><a href="#" class="block px-4 py-2 text-gray-100 hover:bg-gray-700">Dispensación</a></li>
            </ul>
          </div>

          <!-- Estudios Clinicos -->
          <div class="menu-item">
            <a href="#" @click.prevent="toggleMenu('eclinico')" class="flex items-center px-4 py-2 text-gray-100 hover:bg-gray-700">
              <img src="../assets/img/Estudio Clinico.webp" alt="Descripción de la imagen" width="35" height="50" class="mr-2">
              Estudios Clinicos
            </a>
            <ul v-show="menus.eclinico" class="submenu ml-8">
              <li><a href="#" class="block px-4 py-2 text-gray-100 hover:bg-gray-700">Estudios</a></li>
              <li><a href="#" class="block px-4 py-2 text-gray-100 hover:bg-gray-700">Rsultado de Estudios</a></li>
            </ul>
          </div>

          <!-- Transplante -->
          <div class="menu-item">
            <a href="#" @click.prevent="toggleMenu('transplante')" class="flex items-center px-4 py-2 text-gray-100 hover:bg-gray-700">
              <img src="../assets/img/Transplante.webp" alt="Descripción de la imagen" width="35" height="50" class="mr-2">
              Transplante
            </a>
            <ul v-show="menus.transplante" class="submenu ml-8">
              <li><a href="#" class="block px-4 py-2 text-gray-100 hover:bg-gray-700">Solicitud de Transplante</a></li>
              <li><a href="#" class="block px-4 py-2 text-gray-100 hover:bg-gray-700">Organos</a></li>
              <li><a href="#" class="block px-4 py-2 text-gray-100 hover:bg-gray-700">Detalle Organo</a></li>
            </ul>
          </div>

          <!-- Cirugía -->
          <div class="menu-item">
            <a href="#" @click.prevent="toggleMenu('cirugia')" class="flex items-center px-4 py-2 text-gray-100 hover:bg-gray-700">
              <img src="../assets/img/Cirugia.webp" alt="Descripción de la imagen" width="35" height="50" class="mr-2">
              Programacion Quirugica
            </a>
            <ul v-show="menus.cirugia" class="submenu ml-8">
              <li><a href="#" class="block px-4 py-2 text-gray-100 hover:bg-gray-700">Cirugia</a></li>
              <li><a href="#" class="block px-4 py-2 text-gray-100 hover:bg-gray-700">Calendario de Cirugia</a></li>
            </ul>
          </div>
          <!-- Cerrar Sesión -->
          <br>
          <RouterLink to="/">
            <a href="#" class="flex items-center px-4 py-2 mt-2 text-gray-100 hover:bg-gray-700">
              <img src="../assets/img/Cerrar-Sesion.webp" alt="Descripción de la imagen" width="50" height="50" class="mr-2">
              Cerrar Sesión
            </a>
          </RouterLink>

        </nav>
      </div>
    </div>

    <!-- Main content -->
    <div class="flex flex-col flex-1 overflow-y-auto">
      <div class="flex items-center justify-between h-16 bg-white border-b border-gray-200">
        <div class="flex items-center px-4">
          <button class="text-gray-500 focus:outline-none focus:text-gray-700">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
          <input class="mx-4 w-full border rounded-md px-4 py-2" type="text" placeholder="Search">
        </div>
        <div class="flex items-center pr-4">
          <button class="flex items-center text-gray-500 hover:text-gray-700 focus:outline-none focus:text-gray-700">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l-7-7 7-7m5 14l7-7-7-7" />
            </svg>
          </button>
        </div>
      </div>
      
      <!-- <div class="p-4">
        <h1 class="text-2xl font-bold">Dirección General Hospitalaria</h1>
        <p class="mt-2 text-gray-600">Descripcion Princial.</p>
      </div> -->

      <!-- importa los componentes al la vista del Dashboart -->
      <router-view/> 


    </div>
  </div>
</template>



<script>

// import { RouterLink } from 'vue-router';

export default {

  //  components: {
  //   RouterLink,

  // },

  data() {
    return {
      menus: {
        general: false,
        hr: false,
        rmedicos: false,
        pediatria: false,
        farmacia: false,
        eclinico: false,
        transplante: false,
        cirugia: false,
        // Agrega más estados de menú según sea necesario
      }
    };
  },


  methods: {
    toggleMenu(menu) {
      // Cerrar todas las secciones del menú
      for (let menuName in this.menus) {
        if (menuName !== menu) {
          this.menus[menuName] = false;
        }
      }
      // Abrir o cerrar la sección clicada
      this.menus[menu] = !this.menus[menu];
    }
  }
};
</script>

<style scoped>
/* Elimina esta parte
.submenu {
  display: none;
}
*/
</style>