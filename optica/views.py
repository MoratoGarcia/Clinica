from django.shortcuts import render
from django.views.generic import View
# Herramienta para restringir acceso
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class Ncita(View):
	@method_decorator(login_required(login_url='login'))
	def get(self,request):
		template="optica/nueva_cita.html"
		context={
		
		}
		return render(request,template,context)
