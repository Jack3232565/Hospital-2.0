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
                <label for="" class="mb-2 dark:text-gray-300">Nombre</label>
                <input v-model="form.nombre" type="text" required class="mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800" placeholder="Tu Nombre">
              </div>
              <div class="w-full mb-4 lg:mt-6">
                <label for="" class=" dark:text-gray-300">Apellido Paterno</label>
                <input v-model="form.apellidoPaterno" type="text" required class="mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800" placeholder="Primer Apellido">
              </div>
              <div class="w-full mb-4 lg:mt-6">
                <label for="" class=" dark:text-gray-300">Apellido Materno</label>
                <input v-model="form.apellidoMaterno" type="text" required class="mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800" placeholder="Segundo Apellido">
              </div>
            </div>

            <div class="flex lg:flex-row md:flex-col sm:flex-col xs:flex-col gap-2 justify-center w-full">
              <div class="w-full">
                <h3 class="dark:text-gray-300 mb-2">Sexo</h3>
                <select v-model="form.sexo" id="genero" class="w-full text-grey border-2 rounded-lg p-4 pl-2 pr-2 dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800">
                  <option disabled value="">Selecciona tu Sexo</option>
                  <option value="Male">Hombre</option>
                  <option value="Female">Mujer</option>
                </select>
              </div>
              <div class="w-full">
                <h3 class="dark:text-gray-300 mb-2">Tipo de Sangre</h3>
                <select v-model="form.tipoSangre" id="sangre" class="w-full text-grey border-2 rounded-lg p-4 pl-2 pr-2 dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800">
                  <option disabled value="">Selecciona tu Tipo de Sangre</option>
                  <option value="A+">A+</option>
                  <option value="O-">O-</option>
                  <option value="B+">B+</option>
                  <option value="AB+">AB+</option>
                  <option value="A-">A-</option>
                  <option value="O-">O-</option>
                  <option value="B-">B-</option>
                  <option value="AB-">AB-</option>
                </select>
              </div>

              <div class="w-full">
                <h3 class="dark:text-gray-300 mb-2">Fecha de Nacimiemto</h3>
                <input v-model="form.fechaNacimiento" type="date" required class="text-grey p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800">
              </div>
            </div>

            <div class="flex lg:flex-row md:flex-col sm:flex-col xs:flex-col gap-2 justify-center w-full">
              <div class="w-full mb-4 mt-6">
                <label for="" class="mb-2 dark:text-gray-300">CURP</label>
                <input v-model="form.CURP" type="text" required class="mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800" placeholder="Tu CURP">
              </div>
              <div class="w-full mb-4 lg:mt-6">
                <label for="" class=" dark:text-gray-300">Teléfono</label>
                <input v-model="form.telefono" type="text" required class="mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800" placeholder="(52)">
              </div>
              <div class="w-full mb-4 lg:mt-6">
                <label for="" class=" dark:text-gray-300">Correo Electronico</label>
                <input v-model="form.correo" type="email" required class="mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800" placeholder="Tu Correo">
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
