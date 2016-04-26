from django.conf.urls import url
from . import views



urlpatterns=[

	url(r'^$',
		views.SelectPaciente.as_view(),
		name="paciente"),

	url(r'^(?P<paciente_id>\d+)/$',
		views.Ncita.as_view(),
		name="nueva_cita"),


]