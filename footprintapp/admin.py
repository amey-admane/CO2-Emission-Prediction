from django.contrib import admin

# Register your models here.
from .models import carbonfootprintModel,co2predictModel,co2predictionModel

# admin.site.register(co2predictionModel)
admin.site.register(carbonfootprintModel)

admin.site.register(co2predictionModel)