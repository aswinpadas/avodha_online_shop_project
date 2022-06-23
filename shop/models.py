import datetime
from django.db import models


# Create your models here.


class Categ(models.Model):
    categName = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.slug


class Products(models.Model):
    product_name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=400, unique=True)
    product_img = models.ImageField(upload_to='products')
    product_shot_feature = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    price = models.IntegerField()
    cateName = models.ForeignKey(Categ, on_delete=models.CASCADE)

    def __str__(self):
        if (int(self.stock) > 0):
            self.available = True
            self.save()
        else:
            self.available = False
            self.save()
        return self.slug


# class Cart(models.Model):
#     id = models.CharField(max_length=100, unique=True,primary_key=True)
#     date = models.DateField()
#     qty = models.IntegerField()
#     product_id = models.ForeignKey(Products, on_delete=models.CASCADE,related_name='product_id')
#
#     def __str__(self):
#         self.date = datetime.date.today()
