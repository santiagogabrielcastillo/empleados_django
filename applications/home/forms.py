from django import forms 
from .models import Prueba


class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad'
            )
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese su título aquí'
                }
            )
        }
        
        
        
        
    def clean_cantidad(self):
        cant = self.cleaned_data['cantidad']
        if int(cant) <=  10:
            raise forms.ValidationError('La cantidad debe ser mayor a 10')
        return cant
