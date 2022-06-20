from django.shortcuts import render

# Create your views here.
from shop.models import Products, Cart

def createCartId(req):
    c_id=req.session_key
    if not c_id:
        c_id=req.session.create()
    return c_id

def addToCart(req, slug):
    try:

        cart_obj = Cart()
        cart_obj.product_id=prod_obj.slug
        cart_obj.qty=1
        cart_obj.save()
    return render(req,'cart.html',)