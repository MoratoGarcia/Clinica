from django.shortcuts import render
from django.views.generic import View



class Ncita(View):
	def get(self,request):
		template="optica/nueva_cita.html"
		context={
		
		}
		return render(request,template,context)
