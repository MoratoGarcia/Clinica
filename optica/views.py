from django.shortcuts import render, get_object_or_404,redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
# Herramienta para restringir acceso
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# formularios paciente
from .forms import SelecPacienteForm, PacienteForm, ChequeoForm
# modelos
from .models import Paciente


class SelectPaciente(View):
	@method_decorator(login_required(login_url='login'))
	def get(self,request):
		template="optica/nueva_cita.html"
		pacienteform=SelecPacienteForm()
		pacientes=Paciente.objects.all()
		context={
		'pacientes':pacientes,
		'pform':pacienteform,
		
		}
		return render(request,template,context)

	def post(self,request):
		# pacienteform=SelecPacienteForm(request.POST)
		paciente_id=request.POST.get('paciente')
		print(paciente_id)
		return redirect('optica:nueva_cita',paciente_id=paciente_id)

class Ncita(View):
	@method_decorator(login_required(login_url='login'))
	def get(self,request,paciente_id):
		paciente=get_object_or_404(Paciente,pk=paciente_id)
		chequeos=paciente.optexp.chequeos.all().order_by('-fecha')
		cform=ChequeoForm()
		template="optica/detalle.html"
		context={
		'paciente':paciente,
		'chequeos':chequeos,
		'cform':cform,
		}
		return render(request,template,context)

	def post(self,request,paciente_id):
		paciente=get_object_or_404(Paciente,pk=paciente_id)
		new_cform=ChequeoForm(request.POST)
		if new_cform.is_valid():
			new_chequeo=new_cform.save(commit=False)
			new_chequeo.expediente=paciente.optexp
			new_chequeo.save()
		return redirect('optica:nueva_cita',paciente_id=paciente.id)




