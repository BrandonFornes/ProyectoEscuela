from django.urls import include, path
from mi_aplicacion.views import Home, Escuelas,EscuelaAlta, EscuelaEditar, EscuelaEliminar, Maestros , MaestroAlta, MaestroEditar, MaestroEliminar, Alumnos, AlumnoAlta, AlumnoEditar, AlumnoEliminar
from rest_framework import routers
from mi_aplicacion.viewsets import EscuelaViewSet, MaestroViewSet, AlumnoViewSet, UserViewSet, GroupViewSet, PermissionViewSet

router = routers.DefaultRouter()
router.register(r"escuelas", EscuelaViewSet)
router.register(r"maestros", MaestroViewSet)
router.register(r"alumnos", AlumnoViewSet)
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)
router.register(r"permissions", PermissionViewSet)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('api/', include(router.urls)),
    path('escuelas/', Escuelas.as_view(), name='escuelas'),
    path('escuela_alta/', EscuelaAlta.as_view(), name='escuela_alta'),
    path('escuela_editar/<int:id>', EscuelaEditar.as_view(), name='escuela_editar'),
    path('escuela_eliminar/<int:id>', EscuelaEliminar.as_view(), name='escuela_eliminar'),
    path('maestros/', Maestros.as_view(), name='maestros'),
    path('maestro_alta/', MaestroAlta.as_view(), name='maestro_alta'),
    path('maestro_editar/<int:id>', MaestroEditar.as_view(), name='maestro_editar'),
    path('maestro_eliminar/<int:id>', MaestroEliminar.as_view(), name='maestro_eliminar'),
    path('alumnos/', Alumnos.as_view(), name='alumnos'),
    path('alumno_alta/', AlumnoAlta.as_view(), name='alumno_alta'),
    path('alumno_editar/<int:id>', AlumnoEditar.as_view(), name='alumno_editar'),
    path('alumno_eliminar/<int:id>', AlumnoEliminar.as_view(), name='alumno_eliminar'),
]