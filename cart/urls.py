from django.urls import path
from . import views

urlpatterns=[
    path('cart/<str:id>/',views.addToCart,name='cart'),
]