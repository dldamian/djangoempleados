from django.urls import path, include
from .views import (
    ListarTodosEmpleados, EmpleadoPorArea, EmpleadosKeyword,
    ListarHabilidades, EmpleadoDetalles, EmpleadoCreateView,
    SuccessView, EmpleadoActualizar, EliminarEmpleado, Index,
    ListaEmpleadosAdmin
)

app_name = 'personal_app'

urlpatterns = [
    path('listar-todo/', ListarTodosEmpleados.as_view(), name='listaempleados'),
    path('empleado-area/<area>', EmpleadoPorArea.as_view(), name='empleados-area'),
    path('buscar-empleado/', EmpleadosKeyword.as_view()),
    path('habilidades/', ListarHabilidades.as_view()),
    path('ver-detalle/<pk>', EmpleadoDetalles.as_view(), name='ver-detalle'),
    path('agregar-empleado/', EmpleadoCreateView.as_view(), name='agregar-empleado'),
    path('exito/', SuccessView.as_view(), name='exito'),
    path('actualizar-empleado/<pk>', EmpleadoActualizar.as_view(), name='actualizar_empleado'),
    path('eliminar-empleado/<pk>', EliminarEmpleado.as_view(), name='eliminar-empleado'),
    path('', Index.as_view(), name='index'),
    path('empleados-admin', ListaEmpleadosAdmin.as_view(), name='empleados-admin'),
]