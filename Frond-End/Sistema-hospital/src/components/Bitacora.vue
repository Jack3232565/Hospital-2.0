<template>
  <div fluid>
    <b-row>
      <b-col sm="12">
        <h1 style="text-align: center; font-size: 30px">
          Bitácora de Dirección del Hospital
        </h1>
        <br>
        <b-row sm="12">
          <div style="margin-left: auto; margin-right: auto; max-width: 1200px">
            <div class="d-flex flex-wrap justify-content-between">
              <!-- Utilizamos flex-wrap y justify-content-center para centrar los elementos y permitir que se envuelvan en pantallas más pequeñas -->
              <div
              class="md:w-1/2 lg:w-1/4 p-4"
                v-for="(category, index) in categories"
                :key="index"
              >
                <div body-class="rounded">
                  <div>
                    <div
                      class="d-flex align-items-center justify-content-between"
                    >
                      <div class="text-center">
                        <h4 class="mb-2 mt-2">{{ category.title }}</h4>
                        <h3 class="mb-0 line-height">
                          <span
                            ><count-up
                              :end-val="category.value"
                              duration="5"
                            ></count-up
                          ></span>
                        </h3>
                      </div>
                      <div
                        :class="'w-16 h-16 rounded-full flex items-center justify-center ' + category.iconBg">
                        <i :class="category.icon"></i>
                    </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </b-row>
      </b-col>

      <!-- Encabezados -->

      <b-col lg="12">
        <div>
          <div>
            <!--                 
              <div style="margin-left: auto; margin-right: auto; max-width: 1200px">
                <div class="row">

                  <b-col md="6" lg="6">
                    <div>
                      <div v-slot:body>
                        <div class="text-center">
                          <button style="margin: 0 auto; max-width: 200px;" class="btn btn-primary" onclick="window.location.href='/estrucutura-organica-hospital2'">Servicios Medicos</button>
                        </div>
                      </div>
                    </div>
                  </b-col>
                </div>
              </div> -->

            <!-- --------------------------------------------------------- -->
            <nav class="flex items-center justify-between bg-white p-4 shadow-md">
              <div class="flex items-center">
                <div class="relative w-full lg:w-100">
                  <form action="#" class="flex items-center w-full">
                    <input
                      type="text"
                      class="border border-gray-300 rounded-full pl-4 pr-12 py-2 bg-gray-50 focus:outline-none focus:border-blue-500 w-full placeholder-gray-500"
                      title="searchField"
                      placeholder="Buscar"
                      v-model="searchInput"
                    />
                    <button class="absolute right-0 mr-3 text-gray-500 hover:text-gray-700">
                      <i class="ri-search-line"></i>
                    </button>
                  </form>
                </div>
              </div>
              <div class="flex items-center">
                <button @click="miniSidebar" class="flex items-center justify-center w-10 h-10 rounded-full hover:bg-gray-100 focus:outline-none">
                  <i class="ri-more-fill"></i>
                </button>
                <button class="ml-4 lg:hidden focus:outline-none" @click="toggleNav">
                  <i class="ri-menu-3-line text-xl"></i>
                </button>
                <div class="hidden lg:flex items-center ml-4">
                  <slot name="responsiveRight" />
                </div>
                <div class="hidden lg:flex items-center ml-4">
                  <slot name="right" />
                </div>
              </div>
            </nav>

            <!-- <database-website-component :entries="dataset" :columns="dataColumns" :filter-key="searchInput">
                </database-website-component> -->

            <!-- --------------------------------------------------------- -->
          </div>

          <div>
            <div class="overflow-x-auto mb-5">
              <table class="min-w-full border mt-2 table mb-3 table-borderless table-hover">
                <thead>
                  <tr class="text-center">
                    <th class="border px-4 py-2">N°</th>
                    <th class="border px-4 py-2">Tabla</th>
                    <th class="border px-4 py-2">Usuario</th>
                    <th class="border px-4 py-2">Operación</th>
                    <th class="border px-4 py-2">Descripción</th>
                    <th class="border px-4 py-2">Fecha</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(bitacora, id) in paginatedData" :key="id" class="text-center">
                    <td class="border px-4 py-2">{{ bitacora.id }}</td>
                    <td class="border px-4 py-2">{{ bitacora.nombre_tabla }}</td>
                    <td class="border px-4 py-2">{{ bitacora.usuario }}</td>
                    <td class=" ">
                      <div v-if="bitacora.operacion === 'Insert'" class="flex flex-col items-center text-green-600">
                        <a class="flex items-center" target="_self">
                          <i class="fas fa-plus-circle"></i>
                          <span class="ml-2">Agregado</span>
                        </a>
                      </div>
                      <div v-else-if="bitacora.operacion === 'Update'" class="flex flex-col items-center text-orange-600">
                        <a class="flex items-center" target="_self">
                          <i class="fas fa-edit"></i>
                          <span class="ml-2">Actualizado</span>
                        </a>
                      </div>
                      <div v-else-if="bitacora.operacion === 'Delete'" class="flex flex-col items-center text-red-600">
                        <a class="flex items-center" target="_self">
                          <i class="fas fa-trash"></i>
                          <span class="ml-2">Eliminado</span>
                        </a>
                      </div>
                      <div v-else-if="bitacora.operacion === 'Read'" class="flex flex-col items-center text-black">
                        <a class="flex items-center" href="#" target="_self">
                          <i class="fas fa-eye"></i>
                          <span class="ml-2">Lectura</span>
                        </a>
                      </div>
                      <div v-else class="col-12 col-md-6 col-lg-3">
                        {{ bitacora.operacion }}
                      </div>
                    </td>
                    <td class="border px-4 py-2">{{ formatearDescripcion(bitacora.descripcion) }}</td>
                    <td class="border px-4 py-2">{{ formatearFecha(bitacora.fecha_hora) }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
            

            <div class="pagination">
              <button
                class="btn btn-primary"
                @click="previousPage"
                :disabled="currentPage === 1"
              >
                Anterior
              </button>
              <button
                class="btn btn-primary"
                @click="nextPage"
                :disabled="currentPage === totalPages"
              >
                Siguiente
              </button>
            </div>
          </div>
        </div>
      </b-col>
    </b-row>


  </div>
</template>

<script>



import axios from "axios";
import moment from "moment";

export default {
  name: "EstruOrgaHospital",
  components: {  },
  setup() {
    return {
      
    };
  },
  mounted() {
   
    console.log("DOM is rendered");
    console.log(Object.keys(this.currentBitacora).length);
  },

  created() {
    console.log("DOM is created");
    this.getBitacoras();
    this.fetchData();
  },

  methods: {
    getBitacoras() {
      axios
        .get(this.api + "/v1BitacoraDG/")
        .then((response) => {
          console.log(response.data);
          this.bitacoras = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },

    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },

    formatearFecha(fecha) {
      if (moment(fecha, moment.ISO_8601, true).isValid()) {
        return moment(fecha).format("DD/MM/YYYY HH:mm:ss");
      } else {
        return "Sin Fecha";
      }
    },

    formatearDescripcion(descripcion) {
      // Remover la primera parte "Nuevo registro insertado en Aprobaciones_Servicios:"
      descripcion = descripcion.replace(
        "Nuevo registro insertado en Aprobaciones_Servicios:",
        ""
      );

      // Reemplazar los puntos por punto y salto de línea
      let nuevaDescripcion = descripcion.replace(/\./g, ".\n");
      return nuevaDescripcion;
    },

    fetchData() {
      axios
        .get("http://127.0.0.1:8000/hospital/api/v1vista_operaciones_bitacora/")
        .then((response) => {
          // Actualiza los valores de cada categoría con los datos obtenidos de la API
          this.categories[0].value = response.data[0].inserciones;
          this.categories[1].value = response.data[0].actualizaciones;
          this.categories[2].value = response.data[0].eliminaciones;
        })
        .catch((error) => {
          console.error("Error fetching data: ", error);
        });
    },
  },

  data() {
    return {
      bitacoras: [],
      currentBitacora: {},
      api: "http://127.0.0.1:8000/hospital/api",
      bitacora: {
        id: "",
        nombre_tabla: "",
        usuario: "",
        operacion: "",
        descripcion: "",
        fecha_hora: "",
      },
      searchInput: "",
      currentPage: 1, // Página actual
      resultsPerPage: 10, // Resultados por página

      categories: [
        {
          title: "Agregados",
          value: null,
          iconBg: "bg-success",
          icon: "fa fa-arrow-down",
        },
        {
          title: "Actualizados",
          value: null,
          iconBg: "bg-warning",
          icon: "fa fa-refresh",
        },
        {
          title: "Eliminados",
          value: null,
          iconBg: "bg-danger",
          icon: "fa fa-times",
        },
      ],
    };
  },

  computed: {
    filteredData() {
      // Modifica la función para filtrar según el término de búsqueda
      return this.bitacoras.filter((bitacora) => {
        return Object.values(bitacora).some((value) => {
          return String(value)
            .toLowerCase()
            .includes(this.searchInput.toLowerCase());
        });
      });
    },

    paginatedData() {
      const startIndex = (this.currentPage - 1) * this.resultsPerPage;
      const endIndex = startIndex + this.resultsPerPage;
      return this.filteredData
        .slice(startIndex, endIndex)
        .map((item, index) => {
          return {
            ...item,
            index: startIndex + index + 1, // Ajustar el índice para mantener la secuencia numérica continua
          };
        });
    },

    totalPages() {
      return Math.ceil(this.bitacoras.length / this.resultsPerPage);
    },
  },
};
</script>
