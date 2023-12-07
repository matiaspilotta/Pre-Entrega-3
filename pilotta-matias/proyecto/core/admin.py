from django.contrib import admin

# Register your models here.

from . import models

# Register your models here.


admin.site.register(models.Cliente)
admin.site.register(models.identificador)
admin.site.register(models.Pais)
