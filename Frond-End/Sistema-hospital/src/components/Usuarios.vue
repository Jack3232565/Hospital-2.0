<template>
    <section class="py-10 my-auto dark:bg-gray-900">
      <div class="lg:w-[80%] md:w-[90%] xs:w-[96%] mx-auto flex gap-4">
        <div class="lg:w-[88%] md:w-[80%] sm:w-[88%] xs:w-full mx-auto shadow-2xl p-4 rounded-xl h-fit self-center dark:bg-gray-800/40">
          <div>
            <form @submit.prevent="register">
              <!-- Cover Image -->
              <div class="w-full rounded-sm bg-[url('https://img.freepik.com/foto-gratis/blur-hospital_1203-7972.jpg')] bg-cover bg-center bg-no-repeat items-center">
                <!-- Profile Image -->
                <div class="mx-auto flex justify-center w-[450px] h-[150px] rounded-full bg-cover bg-center bg-no-repeat">
                  <v-container>
                    <img src="../assets/img/Logo propuesto Hospital 1.png" alt="">
                  </v-container>
                </div>
              </div>

              <div class="flex lg:flex-row md:flex-col sm:flex-col xs:flex-col gap-2 justify-center w-full">
                <div class="w-full mb-4 mt-6">
                  <label for="" class="mb-2 dark:text-gray-300">Usuario</label>
                  <input v-model="form.usuario" type="text" required class="mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800" placeholder="Tu Nombre de Usuario">
                </div>
                <div class="w-full mb-4 mt-6">
                  <label for="" class="mb-2 dark:text-gray-300">Contraseña</label>
                  <input v-model="form.contraseña" type="password" required class="mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800" placeholder="Tu Contraseña">
                </div>
                <div class="w-full mb-4 lg:mt-6">
                  <label for="" class=" dark:text-gray-300">Repite Contraseña</label>
                  <input v-model="form.repiteContraseña" type="password" required class="mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800" placeholder="Repite tu Contraseña">
                </div>
              </div>
  
              <div class="mt-4">
                <button type="submit" class="w-full p-2 rounded-lg bg-blue-500 mt-4 text-white text-lg font-semibold">Registrar</button>
              </div>
            </form>
            <div class="w-full rounded-lg bg-blue-500 mt-4 text-white text-lg font-semibold">
              <RouterLink to="/">
                <button class="w-full p-2">Inicia Sesión</button>
              </RouterLink>
            </div>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    data() {
      return {
        form: {
          nombre: '',
          apellidoPaterno: '',
          apellidoMaterno: '',
          sexo: '',
          tipoSangre: '',
          fechaNacimiento: '',
          CURP: '',
          telefono: '',
          correo: '',
          usuario: '',
          contraseña: '',
          repiteContraseña: ''
        }
      };
    },
    methods: {
      register() {
        if (this.form.contraseña !== this.form.repiteContraseña) {
          alert('Las contraseñas no coinciden');
          return;
        }
        // Lógica de registro
        console.log('Registrado:', this.form);
      }
    }
  };
  </script>
  
  <style scoped>
  /* Agrega estilos personalizados si es necesario */
  </style>
  