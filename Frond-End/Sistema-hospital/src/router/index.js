// El Router enlaza todas las rutas del sitio 

import { createRouter, createWebHistory } from 'vue-router'
import Login from '../components/Login.vue' 
import RegisterUser from '../components/registerUser.vue'
import RecuperaPass from '../components/recuperaPasword.vue'
import Dashboart from '../components/Dashboart.vue'
import Personas from '../components/Personas.vue'
import Usuarios from '../components/Usuarios.vue'
import Estadisticas from '../components/DatosEstadisticos.vue'
import EstructuraOrg from '../components/EstrucuturaOH.vue'
import AprobacionSM from '../components/AprobacionSM.vue'
import Bitacora from '../components/Bitacora.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterUser
    },
    {
      path: '/recupera',
      name: 'recupera',
      component: RecuperaPass
    },
    {
      path: '/dashboart',
      name: 'dashboart',
      component: Dashboart,
        children:[
          { path: '/personas',
            name: 'personas',
            component: Personas 
          },
          {
            path: '/estadisticas',
            name: 'estadisticas',
            component: Estadisticas
          },
          {
            path: '/estrucuturaOr',
            name: 'estrucuturaOr',
            component: EstructuraOrg
          },
          {
            path: '/aprobacionSM',
            name: 'aprobacionSM',
            component: AprobacionSM
          },
          {
            path: '/bitacora',
            name: 'bitacora',
            component: Bitacora
          },
          ]
    },
 ]
})

export default router
