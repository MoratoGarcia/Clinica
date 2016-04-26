from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class Paciente(models.Model):
	CHOICES=(
		('opcion1','Opcion1'),
		('opcion2','Opcion2'),
		)
	SEX_CHOICES=(
		('mujer','Mujer'),
		('hombre','Hombre'),
		('otro','Otro')
		)
	estado=models.CharField(max_length=20, choices=CHOICES, default='opcion2')
	nombre=models.CharField(max_length=100)
	edad=models.IntegerField()
	sexo=models.CharField(max_length=10,choices=SEX_CHOICES,default='Mujer')
	direccion=models.TextField()
	fecha_nacimiento=models.DateField(blank=True,null=True)
	edad=models.TextField(max_length=5,blank=True,null=True)
	foto=models.ImageField(upload_to='users/%Y/%m/%d',blank=True)

	def __str__(self):
		return self.nombre

	def get_absolute_url_optica(self):
		return reverse('optica:nueva_cita',args=[self.id])

class OptExp(models.Model):
	paciente=models.OneToOneField(Paciente)
	enfermedad=models.CharField(max_length=200)
	dato2=models.CharField(max_length=100,blank=True,null=True)
	dato3=models.CharField(max_length=100,blank=True,null=True)
	
	def __str__(self):
		return "Expediente optica de {}".format(self.paciente)

class Chequeo(models.Model):
	CHOICES=(
		('opcion1','Opcion1'),
		('opcion2','Opcion2'),
		)
	TUBOS=(
		('tuboGrande','TuboGrande'),
		('TuboChico','tubochico'),
		)
	expediente=models.ForeignKey(OptExp,related_name='chequeos')
	fecha=models.DateTimeField(auto_now=True)
	graduacion=models.CharField(max_length=100,choices=TUBOS,default='TuboChico')
	observaciones=models.TextField()
	compra=models.BooleanField(default=True)
	armazon=models.CharField(max_length=50,choices=CHOICES,default='opcion1')

	def __str__(self):
		return "Consultas del {} de {}".format(self.fecha,self.expediente)






