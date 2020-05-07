from django.shortcuts import render
from .models import Empleado
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, TemplateView, UpdateView,
    DeleteView,
)
from django.views.generic.detail import DetailView

class Index(TemplateView):
    template_name = 'index.html'

class ListarTodosEmpleados(ListView):
    template_name = 'personal/lista_todos.html'
    paginate_by = 5
    #context_object_name = 'lista'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('keyword','')
        lista = Empleado.objects.filter(
            primer_nombre__icontains = palabra_clave
        )
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name = 'personal/lista_admin.html'
    paginate_by = 10
    context_object_name = 'empleados'
    model = Empleado



class EmpleadoPorArea(ListView):
    template_name = 'personal/empleados-area.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        area = self.kwargs['area']
        lista = Empleado.objects.filter(
            departamento__nombre_corto = area
        )
        return lista

class EmpleadosKeyword(ListView):
    #import requests

    template_name = 'personal/keyword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('keyword').title()
        lista = Empleado.objects.filter(
            primer_nombre = palabra_clave
        )
        return lista

class ListarHabilidades(ListView):
    template_name = 'personal/habilidades.html'
    model = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=5)

        return empleado.habilidad.all()

class EmpleadoDetalles(DetailView):
    model = Empleado
    template_name = 'personal/detalles.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetalles, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context

class SuccessView(TemplateView):
    template_name = 'personal/exito.html'

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'personal/agregar.html'
    fields = ['primer_nombre','apellidos','trabajo','departamento','habilidad']
    success_url = reverse_lazy('personal_app:empleados-admin')

    def form_valid(self, form):

        empleado = form.save()
        empleado.nombre_completo = empleado.primer_nombre + ' ' + empleado.apellidos
        empleado.save()

        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoActualizar(UpdateView):
    template_name = 'personal/actualizar.html'
    model = Empleado
    fields = ['primer_nombre','apellidos','trabajo','departamento','habilidad']
    success_url = reverse_lazy('personal_app:empleados-admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('+++++++++++++++++++')
        return super().post(request, *args, **kwargs)


class EliminarEmpleado(DeleteView):
    template_name = 'personal/eliminar.html'
    model = Empleado
    success_url = reverse_lazy('personal_app:empleados-admin')