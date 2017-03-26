from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Feira(models.Model):
    id = models.IntegerField(default=0, null=False, primary_key=True, blank=False)
    long = models.IntegerField(default=0, null=True, blank=True)
    lat = models.IntegerField(default=0, null=True, blank=True)
    setcens = models.IntegerField(default=0, null=True, blank=True)
    areap = models.IntegerField(default=0, null=True, blank=True)
    coddist = models.IntegerField(default=0, null=True, blank=True)
    distrito = models.CharField(null=True, max_length=50, blank=True)
    codsubpref = models.IntegerField(default=0, null=True, blank=True)
    subprefe = models.CharField(null=True, max_length=50, blank=True)
    regiao5 = models.CharField(default='', max_length=6, blank=True)
    regiao8 = models.CharField(default='', max_length=7, blank=True)
    nome_feira = models.CharField(null=True, max_length=50, blank=True)
    registro = models.CharField(default='', max_length=6, blank=True)
    logradouro = models.CharField(null=True, max_length=50, blank=True)
    numero = models.CharField(default=0, max_length=10, null=True, blank=True)
    bairro = models.CharField(null=True, max_length=50, blank=True)
    referencia = models.CharField(null=True, max_length=50, blank=True)

    class Meta:
        db_table = 'feira'
        app_label = 'feirapp'
        managed = True

