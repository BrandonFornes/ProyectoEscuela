from django.contrib import admin

# Register your models here.
from mi_aplicacion.models import Escuela,Maestro, Alumno
admin.site.register(Escuela)
admin.site.register(Maestro)
admin.site.register(Alumno)