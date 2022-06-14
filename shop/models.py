from django.db import models

# Create your models here.
class categ(models.Model):
    categName=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    def __str__(self):
        return self.slug
class products(models.Model):
    product_name=models.CharField(max_length=300,unique=True)
    slug = models.SlugField(max_length=400, unique=True)
    product_img=models.ImageField(upload_to='products')
    desc=models.CharField(max_length=500)
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    cateName=models.ForeignKey(categ,on_delete=models.CASCADE)

    def __str__(self):
        return self.slug