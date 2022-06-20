from django.shortcuts import render
from .models import *


# Create your views here.


def homePage(req):
    prod_obj = Products.objects.all()
    for prod in prod_obj:
        if prod.available == True:
            print('**************')
            # del prod_obj[prod]
    return render(req, 'index.html', {'products': prod_obj})


def productDetails(req, slug):
    cat = Categ.objects.all
    product_obj = Products.objects.get(slug=slug)
    return render(req, 'product_details.html', {'products': product_obj, 'categ': cat})


def addToCart(req, productid):
    cart_obj = Cart(product_id=productid,qty=1)
    cart_obj.save()
    return render(req,'cart.html',)

