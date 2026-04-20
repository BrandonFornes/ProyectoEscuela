from django.shortcuts import redirect, render
from django.views import View
from .models import Escuela,Maestro,Alumno
from .forms import EscuelaForm, MaestroForm, AlumnoForm
from django.contrib import messages

class Home(View):
    def get(self , request):
        cdx={
            "titulo":"Home",
            "subtitulo" : "Bienvenido a mi aplicacion",
            }
        return render(request , "home/home.html", cdx)

class Escuelas(View):
    def get(self , request):
        escuelas = Escuela.objects.all()
        cdx={
        "titulo":"Escuelas",
        "subtitulo":"Listado de escuelas",
        "escuelas":escuelas
        }
        return render(request , "escuelas/escuelas.html", cdx)

class EscuelaAlta(View):
    def get(self , request):
        form = EscuelaForm()
        cdx={
        "titulo":"EscuelaFormulario",
        "subtitulo":"Formulario para crear una escuela",
        "form": form,
        
        }
        return render(request , "escuelas/crud.html", cdx)
    
    def post(self,request):
        form = EscuelaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('escuelas')
        else :
            cdx={
                "titulo":"Escuela",
                "subtitulo":"Formulario para crear una escuela",
                "form":form(),
                "mensaje":"Error al crear la escuela."
            }
        return render(request, 'escuelas/crud.html', cdx)
    
class EscuelaEditar(View):
    def get(self , request,id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(instance=escuela)
        cdx={
        "titulo":"EscuelaFormulario",
        "subtitulo":"Formulario para crear una escuela",
        "form": form,
        
        }
        return render(request , "escuelas/crud.html", cdx)
    
    def post(self, request, id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(request.POST, request.FILES, instance=escuela)
        if form.is_valid():
            form.save()
            return redirect('escuelas')
        return redirect('home')

class EscuelaEliminar(View):
    def get(self , request,id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(instance=escuela)
        cdx={
        "titulo":"EscuelaFormulario",
        "subtitulo":"Formulario para crear una escuela", 
        "form": form,
        
        }
        return render(request , "escuelas/crud.html", cdx)
    
    def post(self, request, id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(request.POST, request.FILES, instance=escuela)
        if form.is_valid():
            escuela.delete()
            return redirect('escuelas')
        return redirect('home')


# Maestros
class Maestros(View):
    def get(self , request):
        if not request.user.has_perm('mi_aplicacion.view_maestro'):
            messages.error(request,f"{request.user.username} No tienes permiso para ver esta pagina")
            return redirect('home')
        maestros = Maestro.objects.all()
        escuelas = Escuela.objects.all()

        nombre_query = request.GET.get('nombre')
        escuela_query = request.GET.get('escuela')

        if nombre_query:
            maestros = maestros.filter(nombre__icontains=nombre_query)
        
        if escuela_query:
            maestros = maestros.filter(escuela_id=escuela_query)
            
        cdx={
        "titulo":"Maestros",
        "subtitulo":"Listado de maestros",
        "maestros":maestros,
        "escuelas" : escuelas
        }
        return render(request , "maestros/maestros.html", cdx)

class MaestroAlta(View):
    def get(self , request):
        cdx={
        "titulo":"MaestroFormulario",
        "subtitulo":"Formulario para dar de alta a un maestro",
        "form": MaestroForm(),
        "fondo" : "bg-success p-3",
        "mensaje" : "Guardar"
        
        }
        return render(request , "maestros/crud.html", cdx)
    
    def post(self,request):
        form = MaestroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('maestros')
        else :
            cdx={
                "titulo":"Maestros",
                "subtitulo":"Formulario para dar de alta a un maestro",
                "form":form(),
                "mensaje":"Error al crear maestro."
            }
        return render(request, 'maestros/crud.html', cdx)
    
class MaestroEditar(View):
    def get(self , request,id):
        maestro = Maestro.objects.filter(id=id).first()
        form = MaestroForm(instance=maestro)
        cdx={
        "titulo":"Maestros",
        "subtitulo":"Formulario para dar de alta a un maestro",
        "form": form,
        "fondo" : "bg-warning p-3",
        "mensaje" : "Modificar"
        }
        return render(request , "maestros/crud.html", cdx)
    
    def post(self, request, id):
        maestro = Maestro.objects.filter(id=id).first()
        form = MaestroForm(request.POST, request.FILES, instance=maestro)
        if form.is_valid():
            form.save()
            return redirect('maestros')
        return redirect('home')

class MaestroEliminar(View):
    def get(self , request,id):
        maestro = Maestro.objects.filter(id=id).first()
        form = MaestroForm(instance=maestro)
        cdx={
        "titulo":"Maestros",
        "subtitulo":"Formulario para dar de alta a un maestro",
        "form": form,
        "fondo" : "bg-danger p-3",
        "mensaje" : "Eliminar"
        
        }
        return render(request , "maestros/crud.html", cdx)
    
    def post(self, request, id):
        maestro = Maestro.objects.filter(id=id).first()
        form = MaestroForm(request.POST, request.FILES, instance=maestro)
        if form.is_valid():
            maestro.delete()
            return redirect('maestros')
        return redirect('home')
    

# Maestros
class Alumnos(View):
    def get(self , request):
        alumnos = Alumno.objects.all()
        cdx={
        "titulo":"Alumnos",
        "subtitulo":"Listado de alumnos",
        "alumnos":alumnos
        }
        return render(request , "alumnos/alumnos.html", cdx)

class AlumnoAlta(View):
    def get(self , request):
        cdx={
        "titulo":"AlumnoFormulario",
        "subtitulo":"Formulario para dar de alta a un alumno",
        "form": AlumnoForm(),
        "fondo" : "bg-success p-3",
        "mensaje" : "Guardar"
        
        }
        return render(request , "alumnos/crud.html", cdx)
    
    def post(self,request):
        form = AlumnoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('alumnos')
        else :
            cdx={
                "titulo":"alumnos",
                "subtitulo":"Formulario para dar de alta a un alumno",
                "form":form,
                "mensaje":"Error al crear alumno."
            }
        return render(request, 'alumnos/crud.html', cdx)
    
class AlumnoEditar(View):
    def get(self , request,id):
        alumno = Alumno.objects.filter(id=id).first()
        form = AlumnoForm(instance=alumno)
        cdx={
        "titulo":"Alumnos",
        "subtitulo":"Formulario para dar de alta a un alumno",
        "form": form,
        "fondo" : "bg-warning p-3",
        "mensaje" : "Modificar"
        }
        return render(request , "alumnos/crud.html", cdx)
    
    def post(self, request, id):
        alumno = Alumno.objects.filter(id=id).first()
        form = AlumnoForm(request.POST, request.FILES, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('alumnos')
        return redirect('home')

class AlumnoEliminar(View):
    def get(self , request,id):
        alumno = Alumno.objects.filter(id=id).first()
        form = AlumnoForm(instance=alumno)
        cdx={
        "titulo":"Alumnos",
        "subtitulo":"Formulario para dar de alta a un alumno",
        "form": form,
        "fondo" : "bg-danger p-3",
        "mensaje" : "Eliminar"
        
        }
        return render(request , "alumnos/crud.html", cdx)
    
    def post(self, request, id):
        alumno = Alumno.objects.filter(id=id).first()
        form = AlumnoForm(request.POST, request.FILES, instance=alumno)
        if form.is_valid():
            alumno.delete()
            return redirect('alumnos')
        return redirect('home')

