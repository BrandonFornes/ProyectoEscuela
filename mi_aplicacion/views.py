from django.shortcuts import redirect, render
from django.views import View
from .models import Escuela,Maestro,Alumno
from .forms import EscuelaForm, MaestroForm

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
        maestros = Maestro.objects.all()
        cdx={
        "titulo":"Maestros",
        "subtitulo":"Listado de maestros",
        "maestros":maestros
        }
        return render(request , "maestros/maestros.html", cdx)

class MaestroAlta(View):
    def get(self , request):
        cdx={
        "titulo":"MaestroFormulario",
        "subtitulo":"Formulario para dar de alta a un maestro",
        "form": MaestroForm(),
        "fondo" : "bg-success p-3"
        
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
        "fondo" : "bg-warning p-3"
        
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
        "fondo" : "bg-danger p-3"
        
        }
        return render(request , "maestros/crud.html", cdx)
    
    def post(self, request, id):
        maestro = Maestro.objects.filter(id=id).first()
        form = MaestroForm(request.POST, request.FILES, instance=maestro)
        if form.is_valid():
            maestro.delete()
            return redirect('maestros')
        return redirect('home')
