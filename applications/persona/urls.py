from django.contrib import admin
from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path('', views.InicioView.as_view(), name='home'),
    path('listar-empleados/', views.ListAllEmpleados.as_view(), name='list_all'),
    path('lista-empleados-admin/', views.ListEmpleadosAdmin.as_view(), name='empleados_admin'),
    path('empleados/<departamento>', views.ListByDepartamentoEmpleado.as_view(), name='empleados_departamento'),
    path('empleados/job/<job>', views.ListByJobEmpleado.as_view()),
    path('buscar-empleado/', views.ListaEmpleadosByKword.as_view()),
    path('empleados_habilidades/', views.ListaHabilidadesEmpleado.as_view()),
    path('ver_empleado/<pk>', views.EmpleadoDetail.as_view(), name='empleado_detalle'),
    path('create_empleado/', views.EmpleadoCreateView.as_view(), name='create'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('update_empleado/<pk>', views.EmpleadoUpdateView.as_view(), name='update'),
    path('delete_empleado/<pk>', views.EmpleadoDeleteView.as_view(), name='delete'),
]
