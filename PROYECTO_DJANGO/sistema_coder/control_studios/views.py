from django.shortcuts import render, redirect

from django.urls import reverse
from control_studios.models import Curso, Estudiante
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView



# Create your views here.

def listar_estudiantes(request):
    contexto={
        "estudiantes": Estudiante.objects.all(),

        
    }
    http_response= render(
        request= request,
        template_name="control_studios/lista_estudiantes.html",
        context=contexto,
        )
    return http_response


def listar_cursos(request):
    contexto={
        "cursos": Curso.objects.all(),
    }
    http_response= render(
        request= request,
        template_name="control_studios/lista_cursos.html",
        context=contexto,
        )
    return http_response


def crear_cursos(request):
   http_response = render(
       request=request,
       template_name='control_studios/formulario_curso_a_mano.html',
   )
   return http_response


def crear_curso(request):
   if request.method == "POST":  #user quiere crear un curso
       data = request.POST 
       nombre = data ['nombre']
       nombre = data ['nombre']
       curso = Curso(nombre=data['nombre'], comision=data['comision'])
       curso.save()
       url_exitosa = reverse('lista_cursos')
       return redirect(url_exitosa)
   else:  # GET
       http_response = render(
            request=request,
            template_name='control_studios/formulario_curso_a_mano.html',
        )
       return http_response


def eliminar_curso(request, id):
   curso = Curso.objects.get(id=id)
   if request.method == "POST":
       curso.delete()
       url_exitosa = reverse('lista_cursos')
       return redirect(url_exitosa)


def editar_curso(request, id):
   curso = Curso.objects.get(id=id)
   if request.method == "POST":
       formulario = CursoFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           curso.nombre = data['nombre']
           curso.comision = data['comision']
           curso.save()
           url_exitosa = reverse('listar_cursos')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': curso.nombre,
           'comision': curso.comision,
       }
       formulario = CursoFormulario(initial=inicial)
   return render(
       request=request,
       template_name='estudiantes/formulario_curso.html',
       context={'formulario': formulario},
   )



#EN VISTAS

class EstudianteListView(ListView):
   model = Estudiante
   template_name = 'control_estudios/lista_estudiantes.html'

class EstudianteCreateView(CreateView):
   model = Estudiante
   fields = ('apellido', 'nombre', 'email', 'dni')
   success_url = reverse_lazy('lista_estudiantes')

class EstudianteDetailView(DetailView):
   model = Estudiante
   success_url = reverse_lazy('lista_estudiantes')

class EstudianteUpdateView(UpdateView):
   model = Estudiante
   fields = ('apellido', 'nombre', 'email', 'dni')
   success_url = reverse_lazy('lista_estudiantes')

class EstudianteDeleteView(DeleteView):
   model = Estudiante
   success_url = reverse_lazy('lista_estudiantes')
