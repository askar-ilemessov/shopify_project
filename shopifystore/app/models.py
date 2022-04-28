from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField
from django.db.models.lookups import In
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15,decimal_places=0,default=0)
    quantity= models.IntegerField(blank=True, default=0)
    
    def __str__(self):
        return self.name
