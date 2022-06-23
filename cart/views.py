from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
# Create your views here.
from cart.models import CartModel
from shop.models import Products
from django.core.exceptions import ObjectDoesNotExist


def createCartId(req):
    c_id = req.session.session_key
    if not req.session.exists(req.session.session_key):
        req.session.create()
        c_id = req.session.create()
    return c_id


# def addToCart(req, slug):
#     prod_obj = Products.objects.get(slug=slug)
#     cart_obj = cart(cart_id=createCartId(req))
#     cart_obj.cart_id = slug
#     cart_obj.product_id=prod_obj.slug
#     cart_obj.product_name = prod_obj.product_name
#     cart_obj.cateName = prod_obj.cateName
#     cart_obj.product_qty=1
#     cart_obj.save()
#     return render(req, 'cart.html', {'cart': cart_obj})
# return HttpResponse('Cart Added')

# return render(req,'cart.html',)
def addToCart(req, id):
    prod_obj = Products.objects.get(id=id)
    try:

        cart_obj = CartModel.objects.get(cart_id=createCartId(req))
        # cart_obj.cart_id = createCartId()
        # cart_obj.product_id = prod_obj
        # cart_obj.product_qty += 1
        # cart_obj.save()
    except CartModel.DoesNotExist:
        cart_obj = CartModel.objects.create(cart_id=createCartId(req),product=prod_obj)
        cart_obj.product_qty += 1
        cart_obj.save()
    cartobj2 = CartModel.objects.all()
    return render(req, 'cart.html', {'cart': cartobj2})
