from django import forms
from .models import Formulario

class FormularioRegistro(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['nombre', 'rfc', 'correo','estado','dependencia', 'telefono', 'rango_valor']
        widgets = {
                    
                    'rango_valor' : forms.NumberInput(
                        attrs={
                            'type': 'range',
                            'min': '0',
                            'max': '200000',
                            'step': '1000',
                            'class': 'form-range',
                            'id': 'rangeInput'
                        }
                        
                    )
                    
                }
        
        