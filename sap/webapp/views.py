from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import *
from webapp.models import *


def login(request):
    # return HttpResponse('Holaaa')
    return render(request, 'login.html')


@login_required
def inicio(request):
    # return HttpResponse('Holaaa')
    return render(request, 'home.html')


"""
def registro(request):
    return render(request, 'registro.html')"""


def contraseña(request):
    return render(request, 'contraseña.html')


def recuperada(request):
    return render(request, 'recuperada.html')


def alumnos(request):
    nombre_alumnos = Alumnos.objects.all()
    # alumno = Alumnos.objects.order_by()
    return render(request, 'alumnos.html', {'alumnos': nombre_alumnos})


def lecciones(request):
    nombre_lecciones = Lecciones.objects.all()
    # alumno = Alumnos.objects.order_by()
    return render(request, 'lecciones.html', {'lecciones': nombre_lecciones})


def calificaciones(request):
    nota = Calificaciones.objects.all()
    return render(request, 'calificaciones.html', {'calificaciones': nota})


def alumnoNuevo(request):
    if request.method == 'POST':
        formaAlumnos = AlumnosForm(request.POST)
        if formaAlumnos.is_valid():
            formaAlumnos.save()
            return redirect('alumno')

    else:
        formaAlumnos = AlumnosForm

        return render(request, 'nuevoAlumno.html', {'foralumno': formaAlumnos})


def editarAlumno(request, id):
    alumno = get_object_or_404(Alumnos, pk=id)
    if request.method == 'POST':
        formaAlumnos = AlumnosForm(request.POST, instance=alumno)
        if formaAlumnos.is_valid():
            formaAlumnos.save()
            return redirect('alumno')

    else:
        formaAlumnos = AlumnosForm(instance=alumno)

    return render(request, 'editar.html', {'foralumno': formaAlumnos})


"""añadido


def editarLeccion(request, id):
    leccion = get_object_or_404(Lecciones, pk=id)
    if request.method == 'POST':
        leccionF = leccionForm(request.POST, instance=leccion)
        if leccionF.is_valid():
            leccionF.save()
            return redirect('leccion')
    else:
        leccion = leccionForm

    return render(request, 'leccion.html', {'formlecc': leccionForm})"""

def anadirLeccion(request):
    if request.method == 'POST':
        formLeccion = leccionForm(request.POST)
        if formLeccion.is_valid():
            formLeccion.save()
            return redirect('leccion')

    else:
        formLeccion = leccionForm

        return render(request, 'agregarLeccion.html', {'formlecc': formLeccion})


def eliminarAlumno(request, id):
    alumno = get_object_or_404(Alumnos, pk=id)
    if alumno:
        alumno.delete()
    return redirect('alumno')


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            messages.success(request, f'Usuario {username} creado')
            return redirect('iniciar')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registro.html', context)
