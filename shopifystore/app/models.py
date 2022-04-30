from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField
from django.db.models.lookups import In
from django.urls import reverse




class Warehouse(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    address = models.CharField(max_length=255, blank=False, null=False)
    city = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15,decimal_places=0,default=0)
    quantity= models.IntegerField(blank=True, default=0)
    warehouse = models.ForeignKey(Warehouse, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
