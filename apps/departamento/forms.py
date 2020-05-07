from django import forms
#from .models

class NuevoDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    nombre_corto = forms.CharField(max_length=20)