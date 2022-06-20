from django.shortcuts import render

# Create your views here.
from shop.models import Products, Cart


def addToCart(req, slug):
    prod_obj=Products.objects.get(slug=slug)
    cart_obj = Cart()
    cart_obj.product_id=prod_obj.slug
    cart_obj.qty=1
    cart_obj.save()
    return render(req,'cart.html',)