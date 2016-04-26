from django.conf.urls import url
from . import views



urlpatterns=[
	url(r'^nueva_cita/$',
		views.Ncita.as_view(),
		name="nueva_cita"),


]