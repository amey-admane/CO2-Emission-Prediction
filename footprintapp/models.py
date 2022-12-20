from django.db import models

# Create your models here.




class co2predictModel(models.Model):
    oil_co2 = models.CharField(max_length= 100,default='')

    oil_co2_per_capita = models.CharField(max_length= 100,default='')
    co2_growth_predt = models.CharField(max_length= 100,default='')

    co2_growth_abs = models.CharField(max_length= 100,default='')

    cumulative_co2 = models.CharField(max_length= 100,default='')

    cumulative_oil_co2 = models.CharField(max_length= 100,default='')
    share_global_co2 = models.CharField(max_length= 100,default='')

    share_global_oil_co2 = models.CharField(max_length= 100,default='')

    share_global_cumulative_co2 = models.CharField(max_length= 100,default='')

    share_global_cumulative_oil_co2 = models.CharField(max_length= 100,default='')
    population = models.CharField(max_length= 100,default='')

   

class co2predictionModel(models.Model):
    oil_co2 = models.CharField(max_length= 100,default='')

    oil_co2_per_capita = models.CharField(max_length= 100,default='')
   
    co2_growth_abs = models.CharField(max_length= 100,default='')

    cumulative_co2 = models.CharField(max_length= 100,default='')

    cumulative_oil_co2 = models.CharField(max_length= 100,default='')
    share_global_co2 = models.CharField(max_length= 100,default='')

    share_global_oil_co2 = models.CharField(max_length= 100,default='')

    share_global_cumulative_co2 = models.CharField(max_length= 100,default='')

    share_global_cumulative_oil_co2 = models.CharField(max_length= 100,default='')
    population = models.CharField(max_length= 100,default='')


class carbonfootprintModel(models.Model):

    electric_bill = models.CharField(max_length= 100,default=None)

    gas_bill = models.CharField(max_length= 100,default=None)

    oil_bill = models.CharField(max_length= 100,default=None)

    currency = models.CharField(max_length= 100,default=None)


    mile = models.CharField(max_length= 100,default=None)