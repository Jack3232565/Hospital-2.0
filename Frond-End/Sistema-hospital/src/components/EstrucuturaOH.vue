<template>
  <b-container fluid>
    <b-row>
      <b-col sm="12">
        <h1 style="text-align: center; font-size: 30px">
          Estructura Orgánica del Hospital
        </h1>

        <b-row sm="12">
          <div style="margin-left: auto; margin-right: auto; max-width: 1200px">
            <div class="d-flex flex-wrap justify-content-between">
              <!-- Utilizamos flex-wrap y justify-content-center para centrar los elementos y permitir que se envuelvan en pantallas más pequeñas -->
              <div class="md:w-1/2 lg:w-1/4 p-4" v-for="(category, index) in categories" :key="index">
                <div class="rounded-lg shadow-lg p-4 bg-white">
                  <div class="flex items-center justify-between">
                    <div class="text-center">
                      <h4 class="mb-2 mt-2 text-lg font-semibold">{{ category.title }}</h4>
                      <h3 class="mb-0 text-2xl font-bold">
                        <span>
                          <count-up :end-val="category.value" duration="5"></count-up>
                        </span>
                      </h3>
                    </div>
                    <div :class="'w-16 h-16 rounded-full flex items-center justify-center ' + category.iconBg">
                      <i :class="category.icon + ' text-3xl'"></i>
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
            <h2 class="card-title">Servicios Hospitalarios</h2>

            <div
              style="margin-left: auto; margin-right: auto; max-width: 1200px"
            >
              <div class="row">
                <!-- <b-col md="6" lg="6">
                    <div>
                      <div v-slot:body>
                        <div class="text-center">
                          <button style="margin: 0 auto;" class="btn btn-primary" onclick="window.location.href='/estrucutura-organica-hospital'">Servicios Hospitalarios</button>
                        </div>
                      </div>
                    </div>
                  </b-col> -->

                <b-col md="6" lg="6">
                  <div>
                    <div>
                      <div class="text-center">
                        <button
                          style="margin: 0 auto; max-width: 200px"
                          class="btn btn-primary"
                          onclick="window.location.href='/estrucutura-organica-hospital2'"
                        >
                          Servicios Medicos
                        </button>
                      </div>
                    </div>
                  </div>
                </b-col>
              </div>
            </div>

            <!-- --------------------------------------------------------- -->
             <!-- Buscador de Palabras Clave -->
             <nav class="flex items-center justify-between bg-white p-4 shadow-md">
              <div class="flex items-center">
                <div class="relative w-full lg:w-96">
                  <form action="#" class="flex items-center w-full">
                    <input
                      type="text"
                      class="border border-gray-600 rounded-full pl-4 pr-12 py-2 bg-gray-50 focus:outline-none focus:border-blue-500 w-full placeholder-gray-500"
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
            <div class="table-responsive mb-5">
              <table class="table mb-3 table-borderless table-hover">
                <thead>
                  <tr>
                    <th scope="col">N°</th>
                    <th scope="col">Nombre</th>
                    <th scope="col">Tipo</th>
                    <th scope="col">Tipo de Intervención</th>
                    <th scope="col">Descripción</th>
                    <th scope="col">Departamento Responsable</th>
                    <th scope="col">Estatus</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(servicio, id) in paginatedData" :key="id">
                    <td style="text-align: center">{{ servicio.id }}</td>
                    <td>{{ servicio.nombre }}</td>
                    <td>{{ servicio.tipo }}</td>
                    <td>{{ servicio.tipo_intervencion }}</td>
                    <td>{{ servicio.descripcion }}</td>
                    <td>
                      <div v-if="servicio.departamento_responsable === 1">
                        <h5>Dirección General</h5>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 2">
                        <span>Junta de Gobierno</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 3">
                        <span>Comités Hospitalarios</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 4">
                        <span>Comiés de Transplantes</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 5">
                        <span>Departamento de Calidad</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 6">
                        <span>Autenticacion a Quejas</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 7">
                        <span>Seguridad paciente</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 8">
                        <span>Programacion Quirurgica</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 9">
                        <span>Sub - Dirección Medica</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 10">
                        <span>Sub - Administrativa</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 11">
                        <span>División de Medicina Interna</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 12">
                        <span>División de Pediatía</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 13">
                        <span>Servicio de Traumatología</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 14">
                        <span>División de Cirugía</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 15">
                        <span>Servicio de Urgencias Adultos</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 16">
                        <span>Quirófano</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 17">
                        <span>Terapia Intensiva</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 18">
                        <span>Quirófano y Anestesiología</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 19">
                        <span>Terapia Intermedia</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 20">
                        <span>Centro de Mezclas</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 21">
                        <span>Radiología e imagen</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 22">
                        <span>Genética</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 23">
                        <span>Laboratorio de Análisis Clinicos</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 24">
                        <span>Hemodialisis</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 25">
                        <span>Laboratorio de Patología</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 26">
                        <span>Rehabilitación Pulmonar</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 27">
                        <span>Medicina Genómica</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 28">
                        <span>Banco de Sangre</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 29">
                        <span>Laboratorio Histocompatibilidad</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 30">
                        <span>Aféresis</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 31">
                        <span>Tele-Robotica</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 32">
                        <span>Jefatura de Enseñanza Médica</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 33">
                        <span>Ética e Investigacion</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 34">
                        <span>Consulta Externa</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 35">
                        <span>Terapia y Rehabilitacion Fisica</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 36">
                        <span>Medicina Legal</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 37">
                        <span>Trabajo Social</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 38">
                        <span>UVEH</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 39">
                        <span>CIES</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 40">
                        <span>Comunicacion Social</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 41">
                        <span>Violencia Intrafamiliar</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 42">
                        <span>Jefatura de Enfermeria</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 43">
                        <span>Sub-jefatura de Enfermeria</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 44">
                        <span>Supervisoras de Turno</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 45">
                        <span>Coordinación Enseñanza Enfermeria</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 46">
                        <span>Jefas de Servicio</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 47">
                        <span>Clinicas y Programas</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 48">
                        <span>Recursos Humanos</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 49">
                        <span>Dietética</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 50">
                        <span>Farmacia Intrahospitalaria</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 51">
                        <span
                          >Coordinación de Asuntos Jurídicos y
                          Administrativos</span
                        >
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 52">
                        <span>Biomédica, Conservación y Mantenimiento</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 53">
                        <span>Validación</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 54">
                        <span>Recursos Materiales</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 55">
                        <span>Servicios Generales</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 56">
                        <span>Recursos Financieros</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 57">
                        <span>Departamento Adtvo. Hemodinamia</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 58">
                        <span>Relaciones Públicas</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 59">
                        <span>Farmacia HGC Seguro Popular</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 60">
                        <span>Enlace Administrativo</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 61">
                        <span>Informatica</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 62">
                        <span>Registros Médicos</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 63">
                        <span>Archivo y Correspondencia</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 64">
                        <span>Almacen</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 65">
                        <span>Hemodialisis</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 66">
                        <span>Insumos Especializados</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 67">
                        <span>Intendencia</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 68">
                        <span>Ropería</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 69">
                        <span>Nivel 7</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 70">
                        <span>Control Gastos Catastroficos</span>
                      </div>
                      <div v-else-if="servicio.departamento_responsable === 71">
                        <span>Tecnologia en la Salud</span>
                      </div>
                      <div v-else class="col-12 col-md-6 col-lg-3">
                        {{ servicio.departamento_responsable }}
                      </div>
                    </td>
                    <td>
                      <div v-if="servicio.estatus === true" class="text-center">
                        <a class="iq-icons-list" target="_self">
                          <div class="icon" style="color: green">
                            <i class="fas fa-check"></i>
                          </div>
                          <span style="color: green">Activo</span>
                        </a>
                      </div>

                      <div v-else-if="servicio.estatus === false" class="text-center">
  <a class="iq-icons-list" target="_self">
    <div class="icon" style="color: orange">
      <i class="fas fa-times"></i>
    </div>
    <span style="color: orange">Inactivo</span>
  </a>
</div>

<div v-else-if="servicio.estatus === 3" class="text-center">
  <a class="iq-icons-list" target="_self">
    <div class="icon" style="color: red">
      <i class="fas fa-ban"></i>
    </div>
    <span style="color: red">Suspendido</span>
  </a>
</div>

<div v-else-if="servicio.estatus === 4" class="text-center">
  <a class="iq-icons-list" href="#" target="_self">
    <div class="icon" style="color: black">
      <i class="fas fa-tools"></i>
    </div>
    <span style="color: black">Mantenimiento</span>
  </a>
</div>

<div v-else class="col-12 col-md-6 col-lg-3">
  {{ servicio.estatus }}
</div>
                    </td>
                    <!-- <td>
                      <a href="#" class="edit" title="">
                        <button
                          class="btn btn-warning btn-sm"
                          @click="editBtn(servicio.id)"
                        >
                          Edita
                        </button>
                      </a>
                      <a href="#" class="edit" title="">
                        <button
                          class="btn btn-danger btn-sm"
                          @click="deleteservicio(servicio.id)"
                        >
                          Elimina
                        </button>
                      </a>
                    </td> -->
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

      <div style="margin-left: auto; margin-right: auto; max-width: 1200px">
        <div style="display: flex; justify-content: space-between">
          <b-col md="6" lg="6">
            <div>
              <div>
                <div
                  class="div-body p-0 rounded"
                  :style="`background: url(('../../assets/images/page-img/imagenes-direccionGeneral/medico.jpg')}) no-repeat scroll center center; background-size: contain;  min-height: 146px;`"
                ></div>
                <h4 class="mb-2 mt-2" style="text-align: center">
                  Aprobación de Servicios Hospitalarios
                </h4>
                <div class="text-center">
                  <button
                    class="btn btn-primary"
                    onclick="window.location.href='/aprobacion-servicios-hospitalarios'"
                  >
                    Conoce Más
                  </button>
                </div>
              </div>
            </div>
          </b-col>

          <!-- <b-col md="6" lg="3">
                <div>
                  <div v-slot:body>
                    <div
                      class="div-body p-0 rounded"
                      :style="`background: url(${require('../../assets/images/page-img/imagenes-direccionGeneral/servicioshospitalarios.jpg')}) no-repeat scroll center center; background-size: contain;  min-height: 146px;`"
                    ></div>
                    <h4 class="mb-2 mt-2" style="text-align: center;">Estructura Organica del Hospital</h4>
                    <div class="text-center">
                      <button class="btn btn-primary" onclick="window.location.href='/estrucutura-organica-hospital'">Conoce Más</button>
                    </div>
                  </div>
                </div>
              </b-col> -->

          <b-col md="6" lg="6">
            <div>
              <div>
                <div
                  class="div-body p-0 rounded"
                  :style="`background: url(('../../assets/images/page-img/imagenes-direccionGeneral/EstadisitcasMedicas.jpg')}) no-repeat scroll center center; background-size: contain;  min-height: 146px;`"
                ></div>
                <h4 class="mb-2 mt-2" style="text-align: center">
                  Dashboard General del Hospital
                </h4>
                <div class="text-center">
                  <button
                    class="btn btn-primary"
                    onclick="window.location.href='/dashboard-general-hospital'"
                  >
                    Conoce Más
                  </button>
                </div>
              </div>
            </div>
          </b-col>
        </div>
      </div>
    </b-row>
  </b-container>
</template>



<script>




import axios from "axios";

export default {
  name: "EstruOrgaHospital",
  components: {  },
  setup() {
    return {
      modules: [],
    };
  },
  mounted() {
    console.log("DOM is rendered");
    console.log(Object.keys(this.currentServicio).length);
  },

  created() {
    console.log("DOM is created");
    this.getServicios();
    this.fetchData();
  },

  methods: {
    getServicios() {
      axios
        .get(this.api + "/v1ServiciosHospitalarios/")
        .then((response) => {
          console.log(response.data);
          this.servicios = response.data;
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

    fetchData() {
      axios
        .get(
          "http://127.0.0.1:8000/hospital/api/v1vista_cantidad_personal_medico/"
        )
        .then((response) => {
          // Actualiza los valores de cada categoría con los datos obtenidos de la API
          this.categories[0].value = response.data[0].medicos;
          this.categories[1].value = response.data[0].enfermeros;
          this.categories[2].value = response.data[0].administrativos;
          this.categories[3].value = response.data[0].directivos;
          this.categories[4].value = response.data[0].apoyo;
          this.categories[5].value = response.data[0].residentes;
          this.categories[6].value = response.data[0].internos;
        })
        .catch((error) => {
          console.error("Error fetching data: ", error);
        });
    },
  },

  data() {
    return {
      servicios: [],
      currentServicio: {},
      api: "http://127.0.0.1:8000/hospital/api",
      servicio: {
        id: "",
        nombre: "",
        tipo: "",
        tipo_intervencion: "",
        descripcion: "",
        departamento_responsable_id: "",
        estatus: "",
      },
      searchInput: "",
      currentPage: 1, // Página actual
      resultsPerPage: 10, // Resultados por página

      categories: [
        {
          title: "Médicos",
          value: null,
          iconBg: "bg-primary",
          icon: "fa fa-user-md",
        },
        {
          title: "Enfermeras",
          value: null,
          iconBg: "bg-info",
          icon: "fa fa-medkit",
        },
        {
          title: "Administrativos",
          value: null,
          iconBg: "bg-danger",
          icon: "fa fa-users",
        },
        {
          title: "Directivos",
          value: null,
          iconBg: "bg-warning",
          icon: "fa fa-user",
        },
        {
          title: "Apoyo",
          value: null,
          iconBg: "bg-success",
          icon: "fa fa-user-plus",
        },
        {
          title: "Residentes",
          value: null,
          iconBg: "bg-secondary",
          icon: "fa fa-stethoscope",
        },
        {
          title: "Internos",
          value: null,
          iconBg: "bg-primary",
          icon: "fa fa-hospital-o",
        },
      ],
    };
  },

  computed: {
    filteredData() {
      // Modifica la función para filtrar según el término de búsqueda
      return this.servicios.filter((servicio) => {
        return Object.values(servicio).some((value) => {
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
      return Math.ceil(this.servicios.length / this.resultsPerPage);
    },
  },
};
</script>