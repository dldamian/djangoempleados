from django.urls import path, include
from .views import NuevoDepartamento, ListaDepartamento

app_name = 'depto_app'

urlpatterns = [
    path('nuevo-departamento/', NuevoDepartamento.as_view(), name="nuevo-departamento"),
    path('lista-departamentos/', ListaDepartamento.as_view(), name='lista-departamentos'),
]