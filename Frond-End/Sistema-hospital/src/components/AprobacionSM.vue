<template>

  <div style="background-color: red;">
    <h1>hola</h1>
  </div>
  <div class="container-fluid"> 
    <h1 style="text-align: center;">
      Operaciones CRUD de Solicitudes de Procedimientos Clínicos
      y Quirúrgicos
    </h1>
    <br>
    <b-row>
      <b-col>
        <div class="grid grid-cols-1 md:grid-cols-4 gap-12">
          <div class="md:col-span-3">
            <h2 class="alert alert-primary text-center">
              Lista de Solicitudes
            </h2>
            <!-- buscador de la tabla   -->
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
            
            
            <div class="overflow-x-auto">
              <table class="min-w-full bg-white border border-gray-300 table-hover">
                <thead >
                  <tr class="bg-gray-200 text-gray-600 uppercase text-xs leading-normal">
                    <th class="py-3 px-6 text-left" >No°</th>
                    <th class="py-3 px-6 text-left">Servicio Solicitado</th>
                    <th class="py-3 px-6 text-left">Departamento Solicitante</th>
                    <th class="py-3 px-6 text-left">Fecha de Solicitud</th>
                    <th class="py-3 px-6 text-left">Estatus</th>
                    <th class="py-3 px-6 text-left">Comentario</th>
                    <th class="py-3 px-6 text-left">Fecha de Aprobación</th>
                    <th class="py-3 px-6 text-left">Acciones</th>
                  </tr>
                </thead>
                <tbody class="text-gray-600 text-xs font-light">
                  <tr
                    v-for="(solicitud, id) in paginatedData"
                    :key="id"
                    class="text-center"
                  >
                    <td class="py-3 px-6 text-left whitespace-nowrap truncate">{{ solicitud.id }}</td>
                    <td class="text-center px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                      <div v-if="solicitud.servicio_paciente === 1" class="flex flex-col items-center text-green-600">
                        <img
                          class="mx-auto"
                          src="../assets/img/Servicios Medicos/1.- Urgencias.png"
                          alt="Urgencias Icono"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Urgencias</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 2
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/2.- Consulta Externa.png"
                          alt="Consulta Externa"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Consulta Externa</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 3
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/3.- Hospitalización.png"
                          alt="Hospitalización"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Hospitalización</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 4
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/4.- Cirugia.png"
                          alt="Cirugia"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Cirugía</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 5
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/5.- Laboratorio Clínico.png"
                          alt="Laboratorio Clínico"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Laboratorio Clínico</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 6
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/6.- Radiología.png"
                          alt="Radiología"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Radiología</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 7
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/7.- Farmacia.png"
                          alt="Farmacia"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Farmacia</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 8
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/8.- Rehabilitación.png"
                          alt="Rehabilitación"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Rehabilitación</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 9
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/9.- Cuidados Intensivos.png"
                          alt="Cuidados Intensivos"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Cuidados Intensivos</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 10
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/10.- Atención Pediática.png"
                          alt="Atención Pediática"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Atención Pediática</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 11
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/11.- Atencion Materno-Infantil.png"
                          alt="Atencion Materno-Infantil"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Atención Materno-Infantil</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 12
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/12.- Atencion Geriatrica.png"
                          alt="Atencion Geriatrica"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Atención Geriatríca</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 13
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/13.- Psiquiatria y Salud Mental.png"
                          alt="Psiquiatria y Salud Mental"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Psiquiatría y Salud Mental</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 14
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/14.- Banco de Sangre.png"
                          alt="Banco de Sangre"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Banco de Sangre</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 15
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/15.- Ginecologia y Obstetricia.png"
                          alt="Ginecologia y Obstetricia"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Ginecología y Obstétricia</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 16
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/16.- Quirofano.png"
                          alt="Quirofano"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Quirófano</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 17
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/17.- Tanatologia.png"
                          alt="Tanatologia"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Tanatología</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 18
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/18.- Infectología.png"
                          alt="Infectología"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Infectología</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 19
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/19.- Cardiología.png"
                          alt="Cardiología"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Cardiología</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 20
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/20.- Neurología.png"
                          alt="Neurología"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Neurología</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 21
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/21.- Endocrinología.png"
                          alt="Endocrinología"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Endocrinología</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 22
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/22.- Oftamología.png"
                          alt="Oftamología"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Oftamología</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 23
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/23.- Otorrinología.png"
                          alt="Otorrinología"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Otorrinología</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 24
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/24.- Gastroenterología.png"
                          alt="Gastroenterología"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Gastroenterología</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 25
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/25.- Nefrología.png"
                          alt="Nefrología"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Nefrología</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 26
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/26.- Dermatología.png"
                          alt="Dermatología"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Dermatología</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 27
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/27.- Hematología.png"
                          alt="Hematología"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Hematología</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 28
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/28.- Oncología.png"
                          alt="Oncología"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Oncología</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 29
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/29.- Alergología e Inmunología.png"
                          alt="Alergología e Inmunología"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Alergología e Inmunología</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 30
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/30.- Medicina Física y Rehabilitación.png"
                          alt="Medicina Física y Rehabilitación"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Medicina Física y Rehabilitación</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 31
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/31.- Medicina Interna.png"
                          alt="Medicina Interna"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">Medicina Interna</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.servicio_paciente === 32
                        "
                      >
                        <img class="mx-auto"
                          src="../assets/img/Servicios Medicos/32.- Medicina Preventiva y Salud Pública.png"
                          alt="Medicina Preventiva y Salud Pública.png"
                          width="32"
                          height="32"
                        />
                        <h5 class="text-sm">
                          Medicina Preventiva y Salud Pública
                        </h5>
                      </div>
                      <div
                        v-else
                        class="col-12 col-md-6 col-lg-3"
                      >
                        {{ solicitud.servicio_paciente }}
                      </div>
                    </td>
                    <td>
                      <div
                        v-if="
                          solicitud.departamento_solicitante === 1
                        "
                      >
                        <h5 class="text-sm ">Dirección General</h5>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante === 2
                        "
                      >
                        <span class="text-sm">Junta de Gobierno</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante === 3
                        "
                      >
                        <span class="text-sm">Comités Hospitalarios</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante === 4
                        "
                      >
                        <span class="text-sm">Comiés de Transplantes</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante === 5
                        "
                      >
                        <span class="text-sm">Departamento de Calidad</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante === 6
                        "
                      >
                        <span class="text-sm">Autenticacion a Quejas</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante === 7
                        "
                      >
                        <span class="text-sm">Seguridad paciente</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante === 8
                        "
                      > 
                        <span class="text-sm">Programacion Quirurgica</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante === 9
                        "
                      >
                        <span class="text-sm">Sub - Dirección Medica</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          10
                        "
                      >
                        <span class="text-sm">Sub - Administrativa</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          11
                        "
                      >
                        <span class="text-sm">División de Medicina Interna</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          12
                        "
                      >
                        <span class="text-sm">División de Pediatía</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          13
                        "
                      >
                        <span class="text-sm">Servicio de Traumatología</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          14
                        "
                      >
                        <span class="text-sm">División de Cirugía</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          15
                        "
                      >
                        <span class="text-sm">Servicio de Urgencias Adultos</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          16
                        "
                      >
                        <span class="text-sm">Quirófano</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          17
                        "
                      >
                        <span class="text-sm">Terapia Intensiva</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          18
                        "
                      >
                        <span class="text-sm">Quirófano y Anestesiología</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          19
                        "
                      >
                        <span class="text-sm">Terapia Intermedia</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          20
                        "
                      >
                        <span class="text-sm">Centro de Mezclas</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          21
                        "
                      >
                        <span class="text-sm">Radiología e imagen</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          22
                        "
                      >
                        <span class="text-sm">Genética</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          23
                        "
                      >
                        <span class="text-sm"
                          >Laboratorio de Análisis Clinicos</span
                        >
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          24
                        "
                      >
                        <span class="text-sm">Hemodialisis</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          25
                        "
                      >
                        <span class="text-sm">Laboratorio de Patología</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          26
                        "
                      >
                        <span class="text-sm">Rehabilitación Pulmonar</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          27
                        "
                      >
                        <span class="text-sm">Medicina Genómica</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          28
                        "
                      >
                        <span class="text-sm">Banco de Sangre</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          29
                        "
                      >
                        <span class="text-sm"
                          >Laboratorio Histocompatibilidad</span
                        >
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          30
                        "
                      >
                        <span class="text-sm">Aféresis</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          31
                        "
                      >
                        <span class="text-sm">Tele-Robotica</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          32
                        "
                      >
                        <span class="text-sm">Jefatura de Enseñanza Médica</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          33
                        "
                      >
                        <span class="text-sm">Ética e Investigacion</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          34
                        "
                      >
                        <span class="text-sm">Consulta Externa</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          35
                        "
                      >
                        <span class="text-sm"
                          >Terapia y Rehabilitacion Fisica</span
                        >
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          36
                        "
                      >
                        <span class="text-sm">Medicina Legal</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          37
                        "
                      >
                        <span class="text-sm">Trabajo Social</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          38
                        "
                      >
                        <span class="text-sm">UVEH</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          39
                        "
                      >
                        <span class="text-sm">CIES</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          40
                        "
                      >
                        <span class="text-sm">Comunicacion Social</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          41
                        "
                      >
                        <span class="text-sm">Violencia Intrafamiliar</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          42
                        "
                      >
                        <span class="text-sm">Jefatura de Enfermeria</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          43
                        "
                      >
                        <span class="text-sm">Sub-jefatura de Enfermeria</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          44
                        "
                      >
                        <span class="text-sm">Supervisoras de Turno</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          45
                        "
                      >
                        <span class="text-sm"
                          >Coordinación Enseñanza Enfermeria</span
                        >
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          46
                        "
                      >
                        <span class="text-sm">Jefas de Servicio</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          47
                        "
                      >
                        <span class="text-sm">Clinicas y Programas</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          48
                        "
                      >
                        <span class="text-sm">Recursos Humanos</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          49
                        "
                      >
                        <span class="text-sm">Dietética</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          50
                        "
                      >
                        <span class="text-sm">Farmacia Intrahospitalaria</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          51
                        "
                      > 
                        <span class="text-sm"
                          >Coordinación de Asuntos Jurídicos y
                          Administrativos</span
                        >
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          52
                        "
                      >
                        <span class="text-sm"
                          >Biomédica, Conservación y
                          Mantenimiento</span
                        >
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          53
                        "
                      >
                        <span class="text-sm">Validación</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          54
                        "
                      >
                        <span class="text-sm">Recursos Materiales</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          55
                        "
                      >
                        <span class="text-sm">Servicios Generales</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          56
                        "
                      >
                        <span class="text-sm">Recursos Financieros</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          57
                        "
                      >
                        <span class="text-sm"
                          >Departamento Adtvo. Hemodinamia</span
                        >
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          58
                        "
                      >
                        <span class="text-sm">Relaciones Públicas</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          59
                        "
                      >
                        <span class="text-sm">Farmacia HGC Seguro Popular</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          60
                        "
                      >
                        <span class="text-sm">Enlace Administrativo</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          61
                        "
                      >
                        <span class="text-sm">Informatica</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          62
                        "
                      >
                        <span class="text-sm">Registros Médicos</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          63
                        "
                      >
                        <span class="text-sm">Archivo y Correspondencia</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          64
                        "
                      >
                        <span class="text-sm">Almacen</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          65
                        "
                      >
                        <span class="text-sm">Hemodialisis</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          66
                        "
                      >
                        <span class="text-sm">Insumos Especializados</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          67
                        "
                      >
                        <span class="text-sm">Intendencia</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          68
                        "
                      >
                        <span class="text-sm">Ropería</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          69
                        "
                      >
                        <span class="text-sm">Nivel 7</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          70
                        "
                      >
                        <span class="text-sm">Control Gastos Catastroficos</span>
                      </div>
                      <div
                        v-else-if="
                          solicitud.departamento_solicitante ===
                          71
                        "
                      >
                        <span class="text-sm">Tecnologia en la Salud</span>
                      </div>
                      <div
                        v-else
                        class="col-12 col-md-6 col-lg-3"
                      >
                        {{ solicitud.departamento_solicitante }}
                      </div>
                    </td>
                    <td class="text-sm">
                      {{
                        formatearFecha(solicitud.fecha_solicitud)
                      }}
                    </td>
                    <td>
                      <div v-if="solicitud.estatus === 'Aprobado'" class="text-center">
                        <a class="iq-icons-list" href="#" target="_self">
                          <div class="icon" style="color: green">
                            <i class="fa fa-check"></i> <!-- Usando FontAwesome icon para Aprobado -->
                          </div>
                          <span style="color: green" class="text-sm">Aprobado</span>
                        </a>
                      </div>
                      <div v-else-if="solicitud.estatus === 'En Proceso'" class="text-center">
                        <a class="iq-icons-list" href="#" target="_self">
                          <div class="icon" style="color: orange">
                            <i class="fa fa-spinner fa-spin"></i> <!-- Usando FontAwesome icon -->
                          </div>
                          <span style="color: orange">En Proceso</span>
                        </a>
                      </div>
                      <div v-else-if="solicitud.estatus === 'No Aprobado'" class="text-center">
                        <a class="iq-icons-list" href="#" target="_self">
                          <div class="icon" style="color: red">
                            <i class="fa fa-times"></i> <!-- Usando FontAwesome icon para No Aprobado -->
                          </div>
                          <span style="color: red" class="text-sm">No Aprobado</span>
                        </a>
                      </div>
                      <div v-else-if="solicitud.estatus === 'Cancelado'" class="text-center">
                        <a class="iq-icons-list" href="#" target="_self">
                          <div class="icon" style="color: black">
                            <i class="fa fa-ban"></i> <!-- Usando FontAwesome icon para Cancelado -->
                          </div>
                          <span style="color: black" class="text-sm">Cancelado</span>
                        </a>
                      </div>
                      <div
                        v-else
                        class="col-12 col-md-6 col-lg-3"
                      >
                        {{ solicitud.estatus }}
                      </div>
                    </td>
                    <td class="text-sm">{{ solicitud.comentarios }}</td>
                    <td class="text-sm">
                      {{
                        formatearFecha(solicitud.fecha_aprobacion)
                      }}
                    </td>
                    <td>
                      <a href="#" class="edit" title="">
                        <button  class="btn btn-warning btn-sm text-sm" @click.prevent="editBtn(solicitud.id)">
                          Edita
                        </button>
                      </a>
                      <a href="#" class="edit" title="">
                        <button class="btn btn-danger btn-sm" @click.prevent="deleteSolicitud(solicitud.id)">
                          Elimina
                        </button>
                      </a>
                    </td>
                  </tr>
                </tbody>
                
            </table>

            </div>


          </div>
    
          
    
                                <!-- Edicion de la Solicitudes -->
          <div class="col-md-11">
            <div v-if=" Object.keys(this.currentSolicitud).length !== 0
            "
          >
            <h2 class="alert alert-warning" role="alert"  >
              Actualiza Solicitud
            </h2>
      
            <form
              @submit.prevent="
                updateSolicitud(currentSolicitud.id)
              "
            >
              <div class="row">
                <div class="col">
                  <div class="form-group">
                    <label class="form-label float-left ml-2" scope="col" 
                      >Servicio</label
                    >
                    <select
                      class="form-control"
                      v-model="
                        currentSolicitud.servicio_paciente
                      "
                    >
                    <option class="text-sm" value="1">Urgencias</option>
                    <option class="text-sm" value="2">Consulta Externa</option>
                    <option class="text-sm" value="3">Hospitalización</option>
                    <option class="text-sm" value="4">Cirugia</option>
                    <option class="text-sm" value="5">Laboratorio Clínico</option>
                    <option class="text-sm" value="6">Radiología</option>
                    <option class="text-sm" value="7">Farmacia</option>
                    <option class="text-sm" value="8">Rehabilitación</option>
                    <option class="text-sm" value="9">Cuidados Intensivos</option>
                    <option class="text-sm" value="10">Atención Pediática</option>
                    <option class="text-sm" value="11">Atencion Materno-Infantil</option>
                    <option class="text-sm" value="12">Atencion Geriatrica</option>
                    <option class="text-sm" value="13">Psiquiatria y Salud Mental</option>
                    <option class="text-sm" value="14">Banco de Sangre</option>
                    <option class="text-sm" value="15">Ginecologia y Obstetricia</option>
                    <option class="text-sm" value="16">Quirofano</option>
                    <option class="text-sm" value="17">Tanatologia</option>
                    <option class="text-sm" value="18">Infectología</option>
                    <option class="text-sm" value="19">Cardiología</option>
                    <option class="text-sm" value="20">Neurología</option>
                    <option class="text-sm" value="21">Endocrinología</option>
                    <option class="text-sm" value="22">Oftamología</option>
                    <option class="text-sm" value="23">Otorrinología</option>
                    <option class="text-sm" value="24">Gastroenterología</option>
                    <option class="text-sm" value="25">Nefrología</option>
                    <option class="text-sm" value="26">Dermatología</option>
                    <option class="text-sm" value="27">Hematología</option>
                    <option class="text-sm" value="28">Oncología</option>
                    <option class="text-sm" value="29">Alergología e Inmunología</option>
                    <option class="text-sm" value="30">Medicina Física y Rehabilitación</option>
                    <option class="text-sm" value="31">Medicina Interna</option>
                    <option class="text-sm" value="32">Medicina Preventiva y Salud Pública</option>
                    </select>
                  </div>
                </div>
              </div>
      
              <div class="col">
                <div class="form-group">
                  <label class="form-label float-left ml-2"
                    >Departamento</label
                  >
                  <select
                    class="form-control"
                    v-model="
                      currentSolicitud.departamento_solicitante
                    "
                  >
                  <option value="1">Dirección General</option>
                  <option value="2">Junta de Gobierno</option>
                  <option value="3">Comiés Hospitalarios</option>
                  <option value="4">Comiés de Transplantes</option>
                  <option value="5">Departamento de Calidad</option>
                  <option value="6">Autenticacion a Quejas</option>
                  <option value="7">Seguridad paciente</option>
                  <option value="8">Programacion Quirurgica</option>
                  <option value="9">Sub - Dirección Medica</option>
                  <option value="10">Sub - Administrativa</option>
                  <option value="11">División de Medicina Interna</option>
                  <option value="12">División de Pediatía</option>
                  <option value="13">Servicio de Traumatología</option>
                  <option value="14">División de Cirugía</option>
                  <option value="15">Servicio de Urgencias Adultos</option>
                  <option value="16">Terapia Intensiva</option>
                  <option value="17">Quirófano y Anestesiología</option>
                  <option value="18">Terapia Intermedia</option>
                  <option value="19">Servicio de Urgencias Pediátricas</option>
                  <option value="20">Centro de Mezclas</option>
                  <option value="21">Radiología e imagen</option>
                  <option value="22">Genética</option>
                  <option value="23">Laboratorio de Análisis Clinicos</option>
                  <option value="24">Hemodialisis</option>
                  <option value="25">Laboratorio de Patología</option>
                  <option value="26">Rehabilitación Pulmonar</option>
                  <option value="27">Medicina Genómica</option>
                  <option value="28">Banco de Sangre</option>
                  <option value="29">Laboratorio Histocompatibilidad</option>
                  <option value="30">Aféresis</option>
                  <option value="31">Tele-Robotica</option>
                  <option value="32">Jefatura de Enseñanza Médica</option>
                  <option value="33">Ética e Investigación</option>
                  <option value="34">Consulta Externa</option>
                  <option value="35">Terapia y Rehabilitacion Fisica</option>
                  <option value="36">Medicina Legal</option>
                  <option value="37">Trabajo Social</option>
                  <option value="38">UVEH</option>
                  <option value="39">CIES</option>
                  <option value="40">Comunicacion Social</option>
                  <option value="41">Violencia Intrafamiliar</option>
                  <option value="42">Jefatura de Enfermeria</option>
                  <option value="43">Sub-Jefatura de Enfermeria</option>
                  <option value="44">Supervisoras de Turno</option>
                  <option value="45">Coordinación Enseñanza Enfermeria</option>
                  <option value="46">Jefas de Servicio</option>
                  <option value="47">Clinicas y Programas</option>
                  <option value="48">Recursos Humanos</option>
                  <option value="49">Dietética</option>
                  <option value="50">Farmacia Intrahospitalaria</option>
                  <option value="51">Coordinación de Asuntos Jurídicos y Administrativos</option>
                  <option value="52">Biomédica, Conservación y Mantenimiento</option>
                  <option value="53">Validación</option>
                  <option value="54">Recursos Materiales</option>
                  <option value="55">Servicios Generales</option>
                  <option value="56">Recursos Financieros</option>
                  <option value="57">Departamento Adtvo. Hemodinamia</option>
                  <option value="58">Relaciones Públicas</option>
                  <option value="59">Farmacia HGC Seguro Popular</option>
                  <option value="60">Enlace Administrativo</option>
                  <option value="61">Informatica</option>
                  <option value="62">Registros Médicos</option>
                  <option value="63">Archivo y Correspondencia</option>
                  <option value="64">Vigilancia</option>
                  <option value="65">Almacen</option>
                  <option value="66">Insumos Especializados</option>
                  <option value="67">Intendencia</option>
                  <option value="68">Ropería</option>
                  <option value="69">Nivel 7</option>
                  <option value="70">Control Gastos Catastroficos</option>
                  <option value="71">Tecnologia en la Salud</option>
                  </select>
                </div>
              </div>
              
      
              <div class="row">
                <div class="col">
                  <div class="form-group">
                    <label class="form-label float-left ml-2"
                      >Fecha de Solicitud</label
                    >
                    <input
                      type="text"
                      class="form-control"
                      v-model="currentSolicitud.fecha_solicitud"
                    />
                  </div>
                </div>
              </div>
    
              <div class="col">
                <div class="form-group">
                  <label class="form-label float-left ml-2"
                    >Estado</label
                  >
                  <select
                    class="form-control"
                    v-model="currentSolicitud.estatus"
                  >
                    <option value="Aprobado">Aprobado</option>
                    <option value="En Proceso">En Proceso</option>
                    <option value="No Aprobado">No Aprobado</option>
                    <option value="Cancelado">Cancelado</option>
                  </select>
                </div>
              </div>
              
      
              <div class="row">
                <div class="col">
                  <div class="form-group">
                    <label class="form-label float-left ml-2"
                      >Comentario</label
                    >
                    <input
                      type="text"
                      class="form-control"
                      v-model="currentSolicitud.comentarios"
                    />
                  </div>
                </div>
              </div>

              <div class="col">
                <div class="form-group">
                  <label class="form-label float-left ml-2"
                    >Fecha de Aprobacion</label
                  >
                  <input
                    type="datetime-local"
                    class="form-control"
                    v-model="
                      currentSolicitud.fecha_aprobacion
                    "
                  />
                </div>
              </div>
              <br>
      
              <button
                type="submit"
                class="btn btn-success float-left ml-2"
              >
                Actualzar
              </button>
            </form>
          </div>
      
            
      
                              <!-- Crear Solicitud  -->
      
            <div v-else>
              <h2 class="alert alert-success">Crea Solicitud</h2>
              <form @submit.prevent="saveSolicitud()">
                <div class="row">
                  <div class="col">
                    <div class="form-group">
                      <label class="form-label float-left ml-2"
                        >Servicio</label
                      >
                      <select
                        class="form-control"
                        v-model="solicitud.servicio_paciente"
                        required
                      >
                        <option value="1">Urgencias</option>
                        <option value="2">Consulta Externa</option>
                        <option value="3">Hospitalización</option>
                        <option value="4">Cirugia</option>
                        <option value="5">Laboratorio Clínico</option>
                        <option value="6">Radiología</option>
                        <option value="7">Farmacia</option>
                        <option value="8">Rehabilitación</option>
                        <option value="9">Cuidados Intensivos</option>
                        <option value="10">Atención Pediática</option>
                        <option value="11">Atencion Materno-Infantil</option>
                        <option value="12">Atencion Geriatrica</option>
                        <option value="13">Psiquiatria y Salud Mental</option>
                        <option value="14">Banco de Sangre</option>
                        <option value="15">Ginecologia y Obstetricia</option>
                        <option value="16">Quirofano</option>
                        <option value="17">Tanatologia</option>
                        <option value="18">Infectología</option>
                        <option value="19">Cardiología</option>
                        <option value="20">Neurología</option>
                        <option value="21">Endocrinología</option>
                        <option value="22">Oftamología</option>
                        <option value="23">Otorrinología</option>
                        <option value="24">Gastroenterología</option>
                        <option value="25">Nefrología</option>
                        <option value="26">Dermatología</option>
                        <option value="27">Hematología</option>
                        <option value="28">Oncología</option>
                        <option value="29">Alergología e Inmunología</option>
                        <option value="30">Medicina Física y Rehabilitación</option>
                        <option value="31">Medicina Interna</option>
                        <option value="32">Medicina Preventiva y Salud Pública</option>
                      </select>
                    </div>
                  </div>
                </div>
      
                <div class="row">
                  <div class="col">
                    <div class="form-group">
                      <label class="form-label float-left ml-2"
                        >Departamento</label
                      >
                      <select
                      class="form-control"
                      v-model="
                        solicitud.departamento_solicitante
                      "
                      required
                    >
                      <option value="1">Dirección General</option>
                      <option value="2">Junta de Gobierno</option>
                      <option value="3">Comiés Hospitalarios</option>
                      <option value="4">Comiés de Transplantes</option>
                      <option value="5">Departamento de Calidad</option>
                      <option value="6">Autenticacion a Quejas</option>
                      <option value="7">Seguridad paciente</option>
                      <option value="8">Programacion Quirurgica</option>
                      <option value="9">Sub - Dirección Medica</option>
                      <option value="10">Sub - Administrativa</option>
                      <option value="11">División de Medicina Interna</option>
                      <option value="12">División de Pediatía</option>
                      <option value="13">Servicio de Traumatología</option>
                      <option value="14">División de Cirugía</option>
                      <option value="15">Servicio de Urgencias Adultos</option>
                      <option value="16">Terapia Intensiva</option>
                      <option value="17">Quirófano y Anestesiología</option>
                      <option value="18">Terapia Intermedia</option>
                      <option value="19">Servicio de Urgencias Pediátricas</option>
                      <option value="20">Centro de Mezclas</option>
                      <option value="21">Radiología e imagen</option>
                      <option value="22">Genética</option>
                      <option value="23">Laboratorio de Análisis Clinicos</option>
                      <option value="24">Hemodialisis</option>
                      <option value="25">Laboratorio de Patología</option>
                      <option value="26">Rehabilitación Pulmonar</option>
                      <option value="27">Medicina Genómica</option>
                      <option value="28">Banco de Sangre</option>
                      <option value="29">Laboratorio Histocompatibilidad</option>
                      <option value="30">Aféresis</option>
                      <option value="31">Tele-Robotica</option>
                      <option value="32">Jefatura de Enseñanza Médica</option>
                      <option value="33">Ética e Investigación</option>
                      <option value="34">Consulta Externa</option>
                      <option value="35">Terapia y Rehabilitacion Fisica</option>
                      <option value="36">Medicina Legal</option>
                      <option value="37">Trabajo Social</option>
                      <option value="38">UVEH</option>
                      <option value="39">CIES</option>
                      <option value="40">Comunicacion Social</option>
                      <option value="41">Violencia Intrafamiliar</option>
                      <option value="42">Jefatura de Enfermeria</option>
                      <option value="43">Sub-Jefatura de Enfermeria</option>
                      <option value="44">Supervisoras de Turno</option>
                      <option value="45">Coordinación Enseñanza Enfermeria</option>
                      <option value="46">Jefas de Servicio</option>
                      <option value="47">Clinicas y Programas</option>
                      <option value="48">Recursos Humanos</option>
                      <option value="49">Dietética</option>
                      <option value="50">Farmacia Intrahospitalaria</option>
                      <option value="51">Coordinación de Asuntos Jurídicos y Administrativos</option>
                      <option value="52">Biomédica, Conservación y Mantenimiento</option>
                      <option value="53">Validación</option>
                      <option value="54">Recursos Materiales</option>
                      <option value="55">Servicios Generales</option>
                      <option value="56">Recursos Financieros</option>
                      <option value="57">Departamento Adtvo. Hemodinamia</option>
                      <option value="58">Relaciones Públicas</option>
                      <option value="59">Farmacia HGC Seguro Popular</option>
                      <option value="60">Enlace Administrativo</option>
                      <option value="61">Informatica</option>
                      <option value="62">Registros Médicos</option>
                      <option value="63">Archivo y Correspondencia</option>
                      <option value="64">Vigilancia</option>
                      <option value="65">Almacen</option>
                      <option value="66">Insumos Especializados</option>
                      <option value="67">Intendencia</option>
                      <option value="68">Ropería</option>
                      <option value="69">Nivel 7</option>
                      <option value="70">Control Gastos Catastroficos</option>
                      <option value="71">Tecnologia en la Salud</option>
                    </select>
                    </div>
                  </div>
                </div>
      
                <div class="row">
                  <div class="col">
                    <div class="form-group">
                      <label class="form-label float-left ml-2"
                        >Fecha de Solicitud</label
                      >
                      <input
                        type="datetime-local"
                        class="form-control"
                        v-model="solicitud.fecha_solicitud"
                        required
                      />
                    </div>
                  </div>
                </div>
      
                <div class="row">
                  <div class="col">
                    <div class="form-group">
                      <label class="form-label float-left ml-2"
                        >Estatus</label
                      >
                      <select
                        class="form-control"
                        v-model="solicitud.estatus"
                        required
                      >
                        <option value="Aprobado">Aprobado</option>
                        <option value="En Proceso">En Proceso</option>
                        <option value="No Aprobado">No Aprobado</option>
                        <option value="Cancelado">Cancelado</option>
                      </select>
                    </div>
                  </div>
                </div>
      
                <div class="row">
                  <div class="col">
                    <div class="form-group">
                      <label class="form-label float-left ml-2"
                        >Comentario</label
                      >
                      <input
                        type="text"
                        class="form-control"
                        v-model="solicitud.comentarios"
                        required
                      />
                    </div>
                  </div>
                </div>
      
                <div class="row">
                  <div class="col">
                    <div class="form-group">
                      <label class="form-label float-left ml-2"
                        >Fecha de Aprobacion</label
                      >
                      <input
                        type="datetime-local"
                        class="form-control"
                        v-model="solicitud.fecha_aprobacion"
                      />
                    </div>
                  </div>
                </div>
                <br>
                <button
                  type="submit"
                  class="btn btn-primary float-left ml-2"
                >
                  Guardar
                </button>
              </form>
            </div>
          </div>

        </div>
      </b-col>
    </b-row>



    <div class="pagination">
        <button class="btn btn-primary" @click="previousPage" :disabled="currentPage === 1">
          Anterior
        </button>
        
        <button class="btn btn-primary" @click="nextPage" :disabled="currentPage === totalPages">
          Siguiente
        </button>
    </div>

    <br>
  
      <div class="container py-3">
        <div class="row">
          <div class="col-md-4 mb-4">
            <div class="bg-white shadow rounded overflow-hidden p-2 hover-zoom">
              <div class="rounded text-center">
                <img
                  src="../assets/img/imagenes-direccionGeneral/servicioshospitalarios.jpg"
                  alt="Estructura Organica Hospitalaria"
                  class="mx-auto d-block"
                  style="width: 390px; height: auto;"
                >
                <h4 class="my-2">Estructura Organica del Hospital</h4>
              </div>
              <div class="text-center">
                <button
                  class="btn btn-primary"
                  onclick="window.location.href='/estrucutura-organica-hospital'"
                >
                  Conoce Más
                </button>
              </div>
            </div>
          </div>
      
          <div class="col-md-4 mb-4">
            <div class="bg-white shadow rounded overflow-hidden p-2 hover-zoom">
              <div class="rounded text-center">
                <img
                  src="../assets/img/imagenes-direccionGeneral/serviciosHospitalarios (2).jpg"
                  alt="Estructura Organica Hospitalaria"
                  class="mx-auto d-block"
                  style="width: 300px; height: auto;"
                >
                <h4 class="my-2">Estructura Organica del Hospital</h4>
              </div>
              <div class="text-center">
                <button
                  class="btn btn-primary"
                  onclick="window.location.href='/estrucutura-organica-hospital'"
                >
                  Conoce Más
                </button>
              </div>
            </div>
          </div>
      
          <div class="col-md-4 mb-4">
            <div class="bg-white shadow rounded overflow-hidden p-2 hover-zoom">
              <div class="rounded text-center">
                <img
                  src="../assets/img/imagenes-direccionGeneral/EstadisitcasMedicas.jpg"
                  alt="Estructura Organica Hospitalaria"
                  class="mx-auto d-block"
                  style="width: 290px; height: auto;"
                >
                <h4 class="my-2">Estadisticas del Hospital</h4>
              </div>
              <div class="text-center">
                <button
                  class="btn btn-primary"
                  onclick="window.location.href='/estrucutura-organica-hospital'"
                >
                  Conoce Más
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      
    

  </div>

  
</template>

<style>
.hover-zoom {
  transition: transform 0.3s;
}

.hover-zoom:hover {
  transform: scale(1.05);
}
</style>

<script>
import axios from 'axios'

import moment from "moment";


const body = document.getElementsByTagName("body");

export default{
  name: "AprobacionServiciosHospitalarios",
    data(){
        return{
        solicitudes: [],
        currentSolicitud: {},
        'api': 'http://127.0.0.1:8000/hospital/api',
        solicitud: {
        id: "",
        servicio_paciente: "",
        departamento_solicitante: "",
        fecha_solicitud: "",
        estatus: "",
        comentarios: "",
        fecha_aprobacion: "",
      },
      searchInput: "",
      currentPage: 1, // Página actual
      resultsPerPage: 10, // Resultados por página

      config: {
        dateFormat: "Y-m-d",
        inline: true,
      },

      chart5: {
        series: [
          { name: "Solcitudes Aprobadas", data: [] },
          { name: "En proceso de aprobación", data: [] },
          { name: "Solicitudes Negadas", data: [] },
          { name: "Solicitudes Canceladas", data: [] },
        ],

        colors: ["#089bab", "#FC9F5B", "#FF0000", "#9b9b9b"],
        chart: {
          type: "bar",
          height: 350,
          stacked: true,
          toolbar: {
            show: true,
          },
          zoom: {
            enabled: true,
          },
        },
        responsive: [
          {
            breakpoint: 480,
            options: {
              legend: {
                position: "bottom",
                offsetX: -10,
                offsetY: 0,
              },
            },
          },
        ],
        plotOptions: {
          bar: {
            horizontal: false,
          },
        },
        xaxis: {
          type: "text",
          categories: [
            "Enero",
            "Febrero",
            "Marzo",
            "Abril",
            "Mayo",
            "Junio",
            "Julio",
            "Agosto",
            "Septiembre",
            "Octubre",
            "Noviembre",
            "Diciembre",
          ],
        },
        legend: {
          position: "right",
          offsetY: 40,
        },
        fill: {
          opacity: 1,
        },
      },
      
        }
    },

    mounted(){
     body[0].classList.add("sidebar-main-menu");
     console.log('DOM is rendered')
     console.log(Object.keys(this.currentSolicitud).length)
     this.getVista();
    },

    unmounted() {
    body[0].classList.remove("sidebar-main-menu");
    },

    created(){
     console.log('DOM is created')
     this.getSolicitudes()
     this.getVista();
    },


    methods: {

    getSolicitudes(){
      axios.get(this.api + "/v1AprobacionesServicios/")
        .then((response) => {
          console.log(response.data);
          this.solicitudes = response.data;
        })
        .catch((error) => {
          console.log(error);
        });

},

    saveSolicitud(){
            // Verifica si no se ha insertado ninguna fecha y hora en fecha_aprobacion
            if (!this.solicitud.fecha_aprobacion) {
              this.solicitud.fecha_aprobacion = null; // Establece fecha_aprobacion como null
            }
            axios.post(this.api + "/v1AprobacionesServicios/", this.solicitud)
              .then((response) => {
                console.log(response.data);
                this.getSolicitudes();
                this.solicitud = {};
              })
              .catch((error) => {
                console.log(error);
              });

      },

editBtn(id){
  console.log(id);
      this.solicitudes.map((solicitud) => {
        if (solicitud.id === id) {
          console.log(solicitud.servicio_paciente_id);
          this.currentSolicitud = {
            id: solicitud.id,
            servicio_paciente: solicitud.servicio_paciente,
            departamento_solicitante: solicitud.departamento_solicitante,
            fecha_solicitud: solicitud.fecha_solicitud,
            estatus: solicitud.estatus,
            comentarios: solicitud.comentarios,
            // Verifica si la fecha de aprobación existe, si no, establece como null
            fecha_aprobacion: solicitud.fecha_aprobacion
              ? solicitud.fecha_aprobacion
              : null,
          };
        }
      });
},

updateSolicitud(id){
      // Verifica si no se ha insertado ninguna fecha y hora en fecha_aprobacion
      if (!this.currentSolicitud.fecha_aprobacion) {
        this.currentSolicitud.fecha_aprobacion = null; // Establece fecha_aprobacion como null
      }
      axios.put(
          this.api + `/v1AprobacionesServicios/${id}/`,
          this.currentSolicitud
        )
        .then((response) => {
          console.log(response.data);
          this.getSolicitudes();
          this.currentSolicitud = {};
        })
        .catch((error) => {
          console.log(error);
        });
},



deleteSolicitud(id) {
      // Buscar la solicitud que se va a eliminar
      const solicitud = this.solicitudes.find(
        (solicitud) => solicitud.id === id
      );

      // Mostrar una alerta de confirmación antes de eliminar la solicitud
      if (
        confirm(`¿Deseas eliminar la solicitud? 
                  - ID: ${solicitud.id}
                  - Servicio: ${solicitud.servicio_paciente}
                  - Departamento solicitante: ${
                    solicitud.departamento_solicitante
                  }
                  - Fecha de Solicitud: ${this.formatearFecha(
                    solicitud.fecha_solicitud
                  )}
                  - Estatus: ${solicitud.estatus}
                  - Comentario: ${solicitud.comentarios}
                  - Fecha de Aprobación: ${this.formatearFecha(
                    solicitud.fecha_aprobacion
                  )}`)
      ) {
        axios.delete(this.api + `/v1AprobacionesServicios/${id}/`, id)
          .then((response) => {
            console.log(response.data);
            this.getSolicitudes();
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },


getVista() {
      axios.get("http://127.0.0.1:8000/hospital/api/v1vista_estado_solicitudes/")
        .then((response) => {
          console.log(response.data);
          console.log("envio");

          // Reiniciar datos de la gráfica
          this.chart5.series.forEach((serie) => {
            serie.data = [];
          });

          // Iterar sobre los datos obtenidos y agregarlos a las series correspondientes
          response.data.forEach((item) => {
            this.chart5.series[0].data.push(item.num_aprobadas);
            this.chart5.series[1].data.push(item.num_en_proceso);
            this.chart5.series[2].data.push(item.num_no_aprobadas);
            this.chart5.series[3].data.push(item.num_canceladas);
          });
        })
        .catch((error) => {
          console.error("Error al obtener las solicitudes:", error);
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
},



computed: {

  // esta en adaptacion a la plantilla

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
      return Math.ceil(this.solicitudes.length / this.resultsPerPage);
    },

    filteredData() {
      // Modifica la función para filtrar según el término de búsqueda
      console.log("Search input:", this.searchInput);
      return this.solicitudes.filter((solicitud) => {
        const matchSearchInput = Object.values(solicitud).some((value) => {
          return String(value)
            .toLowerCase()
            .includes(this.searchInput.toLowerCase());
        });

        // Obtener el texto correspondiente al servicio_paciente_id
        let servicioText = "";
        switch (solicitud.servicio_paciente) {
          case 1:
            servicioText = "Urgencias";
            break;
          case 2:
            servicioText = "Consulta Externa";
            break;
          case 3:
            servicioText = "Hospitalización";
            break;
          case 4:
            servicioText = "Cirugía";
            break;
          case 5:
            servicioText = "Laboratorio Clínico";
            break;
          case 6:
            servicioText = "Radiología";
            break;
          case 7:
            servicioText = "Farmacia";
            break;
          case 8:
            servicioText = "Rehabilitación";
            break;
          case 9:
            servicioText = "Cuidados Intensivos";
            break;
          case 10:
            servicioText = "Atención Pediática";
            break;
          case 11:
            servicioText = "Atención Materno-Infantil";
            break;
          case 12:
            servicioText = "Atención Geriátrica";
            break;
          case 13:
            servicioText = "Psiquiatría y Salud Mental";
            break;
          case 14:
            servicioText = "Banco de Sangre";
            break;
          case 15:
            servicioText = "Ginecología y Obstetricia";
            break;
          case 16:
            servicioText = "Quirófano";
            break;
          case 17:
            servicioText = "Tanatología";
            break;
          case 18:
            servicioText = "Infectología";
            break;
          case 19:
            servicioText = "Cardiología";
            break;
          case 20:
            servicioText = "Neurología";
            break;
          case 21:
            servicioText = "Endocrinología";
            break;
          case 22:
            servicioText = "Oftamología";
            break;
          case 23:
            servicioText = "Otorrinología";
            break;
          case 24:
            servicioText = "Gastroenterología";
            break;
          case 25:
            servicioText = "Nefrología";
            break;
          case 26:
            servicioText = "Dermatología";
            break;
          case 27:
            servicioText = "Hematología";
            break;
          case 28:
            servicioText = "Oncología";
            break;
          case 29:
            servicioText = "Alergología e Inmunología";
            break;
          case 30:
            servicioText = "Medicina Física y Rehabilitación";
            break;
          case 31:
            servicioText = "Medicina Interna";
            break;
          case 32:
            servicioText = "Medicina Preventiva y Salud Pública";
            break;

          default:
            servicioText = String(solicitud.servicio_paciente); // Si no coincide con ninguno, mantener el valor original
        }

        const matchServicioId = servicioText
          .toLowerCase()
          .includes(this.searchInput.toLowerCase());

        let departamentoText = "";
        switch (solicitud.departamento_solicitante) {
          case 1:
            departamentoText = "Dirección General";
            break;
          case 2:
            departamentoText = "Junta de Gobierno";
            break;
          case 3:
            departamentoText = "Comiés Hospitalarios";
            break;
          case 4:
            departamentoText = "Comiés de Transplantes";
            break;
          case 5:
            departamentoText = "Departamento de Calidad";
            break;
          case 6:
            departamentoText = "Autenticacion a Quejas";
            break;
          case 7:
            departamentoText = "Seguridad paciente";
            break;
          case 8:
            departamentoText = "Programacion Quirurgica";
            break;
          case 9:
            departamentoText = "Sub - Dirección Medica";
            break;
          case 10:
            departamentoText = "Sub - Administrativa";
            break;
          case 11:
            departamentoText = "División de Medicina Interna";
            break;
          case 12:
            departamentoText = "División de Pediatía";
            break;
          case 13:
            departamentoText = "Servicio de Traumatología";
            break;
          case 14:
            departamentoText = "División de Cirugía";
            break;
          case 15:
            departamentoText = "Servicio de Urgencias Adultos";
            break;
          case 16:
            departamentoText = "Terapia Intensiva";
            break;
          case 17:
            departamentoText = "Quirófano y Anestesiología";
            break;
          case 18:
            departamentoText = "Terapia Intermedia";
            break;
          case 19:
            departamentoText = "Servicio de Urgencias Pediátricas";
            break;
          case 20:
            departamentoText = "Centro de Mezclas";
            break;
          case 21:
            departamentoText = "Radiología e imagen";
            break;
          case 22:
            departamentoText = "Genética";
            break;
          case 23:
            departamentoText = "Laboratorio de Análisis Clinicos";
            break;
          case 24:
            departamentoText = "Hemodialisis";
            break;
          case 25:
            departamentoText = "Laboratorio de Patología";
            break;
          case 26:
            departamentoText = "Rehabilitación Pulmonar";
            break;
          case 27:
            departamentoText = "Medicina Genómica";
            break;
          case 28:
            departamentoText = "Banco de Sangre";
            break;
          case 29:
            departamentoText = "Laboratorio Histocompatibilidad";
            break;
          case 30:
            departamentoText = "Aféresis";
            break;
          case 31:
            departamentoText = "Tele-Robotica";
            break;
          case 32:
            departamentoText = "Jefatura de Enseñanza Médica";
            break;
          case 33:
            departamentoText = "Ética e Investigacion";
            break;
          case 34:
            departamentoText = "Consulta Externa";
            break;
          case 35:
            departamentoText = "Terapia y Rehabilitacion Fisica";
            break;
          case 36:
            departamentoText = "Medicina Legal";
            break;
          case 37:
            departamentoText = "Trabajo Social";
            break;
          case 38:
            departamentoText = "UVEH";
            break;
          case 39:
            departamentoText = "CIES";
            break;
          case 40:
            departamentoText = "Comunicacion Social";
            break;
          case 41:
            departamentoText = "Violencia Intrafamiliar";
            break;
          case 42:
            departamentoText = "Jefatura de Enfermeria";
            break;
          case 43:
            departamentoText = "Sub-jefatura de Enfermeria";
            break;
          case 44:
            departamentoText = "Supervisoras de Turno";
            break;
          case 45:
            departamentoText = "Coordinación Enseñanza Enfermeria";
            break;
          case 46:
            departamentoText = "Jefas de Servicio";
            break;
          case 47:
            departamentoText = "Clinicas y Programas";
            break;
          case 48:
            departamentoText = "Recursos Humanos";
            break;
          case 49:
            departamentoText = "Dietética";
            break;
          case 50:
            departamentoText = "Farmacia Intrahospitalaria";
            break;
          case 51:
            departamentoText =
              "Coordinación de Asuntos Jurídicos y Administrativos";
            break;
          case 52:
            departamentoText = "Biomédica, Conservación y Mantenimiento";
            break;
          case 53:
            departamentoText = "Validación";
            break;
          case 54:
            departamentoText = "Recursos Materiales";
            break;
          case 55:
            departamentoText = "Servicios Generales";
            break;
          case 56:
            departamentoText = "Recursos Financieros";
            break;
          case 57:
            departamentoText = "Departamento Adtvo. Hemodinamia";
            break;
          case 58:
            departamentoText = "Relaciones Públicas";
            break;
          case 59:
            departamentoText = "Farmacia HGC Seguro Popular";
            break;
          case 60:
            departamentoText = "Enlace Administrativo";
            break;
          case 61:
            departamentoText = "Informatica";
            break;
          case 62:
            departamentoText = "Registros Médicos";
            break;
          case 63:
            departamentoText = "Archivo y Correspondencia";
            break;
          case 64:
            departamentoText = "Vigilancia";
            break;
          case 65:
            departamentoText = "Almacen";
            break;
          case 66:
            departamentoText = "Insumos Especializados";
            break;
          case 67:
            departamentoText = "Intendencia";
            break;
          case 68:
            departamentoText = "Ropería";
            break;
          case 69:
            departamentoText = "Nivel 7";
            break;
          case 70:
            departamentoText = "Control Gastos Catastroficos";
            break;
          case 71:
            departamentoText = "Tecnologia en la Salud";
            break;

          default:
            departamentoText = String(solicitud.departamento_solicitante);
        }

        const matchDepartamentoId = departamentoText
          .toLowerCase()
          .includes(this.searchInput.toLowerCase());

        // console.log("Entrada de búsqueda de coincidencias:", matchSearchInput);
        // console.log(
        //   "Entrada de búsqueda de servicio_paciente_id:",
        //   matchServicioId
        // );
        // console.log(
        //   "Entrada de búsqueda de departamento_solicitante:",
        //   matchDepartamentoId
        // );

        return matchSearchInput || matchServicioId || matchDepartamentoId;
      });
    },
  
},

}
</script>
