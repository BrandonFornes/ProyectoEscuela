from django.urls import path
from mi_aplicacion.views import Home, Escuelas,EscuelaAlta, EscuelaEditar, EscuelaEliminar, Maestros , MaestroAlta, MaestroEditar, MaestroEliminar

urlpatterns = [
path('', Home.as_view(), name='home'),
path('escuelas/', Escuelas.as_view(), name='escuelas'),
path('escuela_alta/', EscuelaAlta.as_view(), name='escuela_alta'),
path('escuela_editar/<int:id>', EscuelaEditar.as_view(), name='escuela_editar'),
path('escuela_eliminar/<int:id>', EscuelaEliminar.as_view(), name='escuela_eliminar'),
path('maestros/', Maestros.as_view(), name='maestros'),
path('maestro_alta/', MaestroAlta.as_view(), name='maestro_alta'),
path('maestro_editar/<int:id>', MaestroEditar.as_view(), name='maestro_editar'),
path('maestro_eliminar/<int:id>', MaestroEliminar.as_view(), name='maestro_eliminar'),
]