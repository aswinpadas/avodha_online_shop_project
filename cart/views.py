from django.http import HttpResponse
from django.shortcuts import render
from . models import cart
# Create your views here.
from shop.models import Products, Cart

def createCartId(req):
    if not req.session.exists(req.session.session_key):
        req.session.create()
        c_id=req.session.create()
        return c_id

def addToCart(req, slug):
    try:
        prod_obj=Products.objects.get(slug=slug)
        cart_obj= cart.objects.get(cart_id=createCartId(req))
        cart_obj.product_id = slug
        cart_obj.product_name = prod_obj.product_name
        cart_obj.save()
        if not cart_obj:
            cart_obj=cart()
            cart_obj.cart_id=createCartId(req)
            cart_obj.product_id=slug
            cart_obj.product_name=prod_obj.product_name
            cart_obj.save()
        return HttpResponse('Cart Added')

    except:
        return HttpResponse('Cart not Added')

    # return render(req,'cart.html',)