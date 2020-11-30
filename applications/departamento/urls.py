from django.contrib import admin
from django.urls import path
from . import views


app_name = "departamento_app"

urlpatterns = [
    path('departamento/', admin.site.urls),
    path('new_departamento/', views.NewDepartamentoView.as_view(), name="new"),
    path('departamentos/', views.DepartamentoListView.as_view(), name="list_all")
]
