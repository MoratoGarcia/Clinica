from django import forms
from .models import Paciente, Chequeo


class SelecPacienteForm(forms.Form):
	paciente = forms.ModelChoiceField(queryset=Paciente.objects.all(), 
                                  label="Paciente")

class PacienteForm(forms.ModelForm):
	class Meta:
		model=Paciente
		fields=['nombre','edad','sexo','direccion','fecha_nacimiento','foto','estado']

class ChequeoForm(forms.ModelForm):
	class Meta:
		model=Chequeo
		fields=['graduacion','observaciones','compra','armazon']