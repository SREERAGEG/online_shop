from django.shortcuts import render
from django.http import HttpResponse
from . models import Product

# Create your views here.
def index(request):
    Products=Product.objects.all()
    return render(request,'index.html',{'products':Products})
    #return HttpResponse("<h1> Welcome to Django</h1>")
def about(requests):
    return HttpResponse("<h1>About page</h1>")

