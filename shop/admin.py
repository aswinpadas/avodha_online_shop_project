from django.contrib import admin
# Register your models here.
from shop.models import *
class categAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('categName',)}
class productAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}

admin.site.register(Categ,categAdmin)
admin.site.register(Products,productAdmin)