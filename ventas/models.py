from django.db import models
from django.conf import settings 
from django.core.urlresolvers import reverse


#Me falta generar algo aquí que nos permita grabar el costo del lente y hacer las evidentes 
#operaciones matemáticas sobre los costos e importes, abonos y todo lo que incluye pagos :S

class Pagos(model.Models):
	STATUS_PAGOS_CHOICES=(
		('pagado','Pagado'),
		('abono','Abonado'),
		('liquidado','Liquidado'),
		('pp','Pago Parcial'),
		('pl','Pago Parcial liquida contraentrega')
		)
	statusPagos=models.CharField(max_length=100, choices=STATUS_PAGOS_CHOICES,default='pagado')
    pagoParcialLiquidaContraentrega=models.CharField(max_length=50,blank=True,null=True,)

	def __str__(self):
		return self.statusPagos

class Descuentos(model.Models):
	DESCUENTOS_INSTITUCIONALES_CHOICES=(
		('10%','Institución1 10%'),
		('20%','Institución2 20%'),
		('30%','Institución3 30%'),
		('40%','Institución4 40%'),
		('50%','Institución5 50%'),
		)
	descuentosInstitucionales=models.CharField(max_length=50, choices=DESCUENTOS_INSTITUCIONALES_CHOICES, default='10%')
	
	def __str__(self):
		return self.descuentosInstitucionales

class Entregas(models.Models):
	STATUS_ENTREGAS_LENTES_CHOICES=(
		('entregado','Entregado a Cliente'),
		('pedido','Pedido a proveedor'),
		('laboratorio','En elaboración'),
		)
	statusEntregas=models.CharField(max_length=100, choices=STATUS_ENTREGAS_LENTES_CHOICES,default='pedido')
	
	def __str__(self):
		return self.statusEntregas

