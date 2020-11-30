from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .models import Empleado
from applications.departamento.models import Departamento
from .forms import EmpleadoForm



class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    #paginación
    paginate_by = 4
    model = Empleado
    ordering = ['first_name']
    context_object_name = 'empleados'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        return Empleado.objects.filter(full_name__icontains=palabra_clave)
    

class ListEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    #paginación
    paginate_by = 10
    model = Empleado
    ordering = ['first_name']
    context_object_name = 'empleados'
    

class ListByDepartamentoEmpleado(ListView):
    """ Lista empleados de un área """
    template_name = 'persona/empleado_por_departamento.html'
    context_object_name = 'empleados'
    
    # saco el parámetro <departamento> desde url, busco el obj con name=parametro y filtro empleado con ese departamento
    def get_queryset(self):
        self.departamento = get_object_or_404(Departamento, name=self.kwargs['departamento'])
        return Empleado.objects.filter(departamento=self.departamento)
    
class ListByJobEmpleado(ListView):
    """ Lista empleados con un trabajo """
    template_name = 'persona/empleado_por_job.html'
    context_object_name = 'empleados'
    def get_queryset(self):
        return Empleado.objects.filter(job=self.kwargs['job'])
    
class ListaEmpleadosByKword(ListView):
    """Lista de empleados por palabra clave"""
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",)
        if palabra_clave:
            return Empleado.objects.filter(first_name=palabra_clave.capitalize())
        
class ListaHabilidadesEmpleado(ListView):
    model = Empleado
    template_name = "persona/habilidades.html"
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        param = self.request.GET.get("id",)
        if param:
            empleado = get_object_or_404(Empleado, id=param)
            return empleado.habilidades.all()
    

class EmpleadoDetail(DetailView):
    model = Empleado
    template_name='persona/empleado_detail.html'
    context_object_name = 'empleado'
   

class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/create.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:list_all')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
    
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    context_object_name = 'empleado'
    fields = ('__all__')
    success_url = reverse_lazy('persona_app:list_all')
    
    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:list')


class InicioView(TemplateView):
    template_name = "home.html"

