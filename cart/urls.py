from django.urls import path
from . import views

urlpatterns=[
    path('cart/<str:slug>/',views.addToCart,name='cart'),
]