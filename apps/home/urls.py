from django.urls import path, include
from .views import (
    PruebaView, PruebaListView, ListarPrueba,
    PruebaCreateView,
    )

urlpatterns = [
    path('prueba/', PruebaView.as_view()),
    path('lista/', PruebaListView.as_view()),
    path('lista-prueba/', ListarPrueba.as_view()),
    path('agregar/', PruebaCreateView.as_view()),
]