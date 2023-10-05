from django.contrib import admin

# Register your models here.
from . models import Product
from . models import offer
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','stock')
admin.site.register(Product,ProductAdmin)
class OfferAdmin(admin.ModelAdmin):
    list_display=('code','discount')
admin.site.register(offer,OfferAdmin)