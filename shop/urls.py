from django.urls import path
from . import views

urlpatterns=[
    path('',views.homePage,name='homePage'),
    path('product_details/<str:slug>/',views.productDetails,name='product_details'),
    path('product_details/<str:slug>/',views.productDetails,name='product_details'),
]