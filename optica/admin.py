from django.contrib import admin
from . import models


admin.site.register(models.Paciente)
admin.site.register(models.Chequeo)
admin.site.register(models.OptExp)



