from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import NuevoDepartamentoForm
from apps.personal.models import Empleado
from .models import Departamento
from django.views.generic import ListView

class ListaDepartamento(ListView):
    template_name = 'departamento/lista.html'
    model = Departamento
    context_object_name = 'departamentos'


class NuevoDepartamento(FormView):
    template_name = 'departamento/nuevo_departamento.html'
    form_class = NuevoDepartamentoForm
    success_url = reverse_lazy('depto_app:lista-departamentos')

    def form_valid(self, form):

        depa = Departamento(
            nombre = form.cleaned_data['departamento'],
            nombre_corto = form.cleaned_data['nombre_corto']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Empleado.objects.create(
            primer_nombre = nombre,
            apellidos = apellidos,
            trabajo = '1',
            departamento = depa


        )
        return super(NuevoDepartamento, self).form_valid(form)