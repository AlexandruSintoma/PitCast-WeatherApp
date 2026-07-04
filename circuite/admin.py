from django.contrib import admin
from . import models

# le inregistrez in admin ca sa le pot vedea si modifica si de acolo
admin.site.register(models.Circuit)
admin.site.register(models.MarePremiu)
admin.site.register(models.Comentariu)
