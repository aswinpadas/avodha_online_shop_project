from datetime import datetime

from django.db import models

# Create your models here.
from django.db.models import CASCADE
from shop.models import Products, Categ


class cart(models.Model):
    cart_id=models.CharField(max_length=300,unique=True)
    date=models.DateField(auto_now_add=True)
    product_name=models.CharField(max_length=300)
    categName=models.ForeignKey(Categ,on_delete=CASCADE)
    product_qty=models.IntegerField()
    product_id=models.ForeignKey(Products,on_delete=CASCADE)

    def __str__(self):
        return self.cart_id
