from django.urls import path
from . import views

urlpatterns=[
    path('accounts/signup', views.signup, name='sign_up'),
    path('accounts/signup', views.districtRender, name='state'),
    path('accounts/signin', views.signin, name='signin'),
]