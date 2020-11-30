from django.contrib import admin
from .models import Empleado, Habilidades

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'email'
        )
    
    def email(self, obj):
        return obj.first_name.lower()+ obj.last_name.lower()+'@mail.com'
    
    def full_name(self, obj):
        #toda la operacion
        print(obj.first_name)
        return obj.first_name + ' ' + obj.last_name
    
    search_fields = ('first_name',)
    list_filter = ('job',)
    filter_horizontal = ('habilidades',)
    ordering = ['id']

admin.site.register(Empleado, EmpleadoAdmin)

