<template>
    <div class="flex justify-center items-center min-h-screen bg-gray-100">
      <div class="bg-white rounded-lg shadow-lg overflow-hidden max-w-md w-full">
        <div class="p-12">
          <h2 class="text-2xl font-semibold text-gray-700 text-center">Hospital General Hopital Care</h2>
          <p class="text-xl text-gray-600 text-center">Registrate</p>
          
          <form @submit.prevent="register">
            <div class="mt-4">
              <label class="block text-gray-700 text-sm font-bold mb-2">Nombre</label>
              <input v-model="form.nombre" class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="text" required />
            </div>
            
            <div class="mt-4">
              <label class="block text-gray-700 text-sm font-bold mb-2">Apellido Paterno</label>
              <input v-model="form.apellidoPaterno" class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="text" required />
            </div>
            
            <div class="mt-4">
              <label class="block text-gray-700 text-sm font-bold mb-2">Apellido Materno</label>
              <input v-model="form.apellidoMaterno" class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="text" required />
            </div>
            
            <div class="mt-4">
              <label class="block text-gray-700 text-sm font-bold mb-2">Correo</label>
              <input v-model="form.correo" class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="email" required />
            </div>
            
            <div class="mt-4">
              <label class="block text-gray-700 text-sm font-bold mb-2">Contraseña</label>
              <input v-model="form.contraseña" class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="password" required />
            </div>
            
            <div class="mt-4">
              <label class="block text-gray-700 text-sm font-bold mb-2">Repite Contraseña</label>
              <input v-model="form.repiteContraseña" class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="password" required />
            </div>
            
            <div class="mt-8">
              <button type="submit" class="bg-gray-700 text-white font-bold py-2 px-4 w-full rounded hover:bg-gray-600">Registrar</button>
            </div>
          </form>
          
          <div class="mt-8 flex items-center justify-between">
            <span class="border-b w-1/5 md:w-1/4"></span>
            <RouterLink to="/">
              <a class="text-gray-700 font-bold hover:underline">Inicia Sesión</a>
            </RouterLink>
            <span class="border-b w-1/5 md:w-1/4"></span>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        form: {
          nombre: '',
          apellidoPaterno: '',
          apellidoMaterno: '',
          correo: '',
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