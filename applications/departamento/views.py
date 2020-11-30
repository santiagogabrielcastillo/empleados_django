from django.shortcuts import render
from .forms import NewDepartamentoForm
from django.views.generic import ListView
from django.views.generic.edit import FormView 
from applications.persona.models import Empleado
from .models import Departamento
from django.urls import reverse_lazy


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = 'departamentos'
 


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = reverse_lazy('departamento_app:list_all')
    
    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        depto = Departamento(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['short_name']
        )
        depto.save()
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento = depto
        )
        return super(NewDepartamentoView, self).form_valid(form)  