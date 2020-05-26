

from django.shortcuts import render, redirect  
#*from django.contrib.auth.forms import UserCreationForm
#*from eatery.forms import EateryForm  
from eatery.models import * 

# Create your views here.
    
def store(request):
    menutables = MenuTable.objects.all()
    context = {'menutables': menutables}
    return render(request, "eatery/store.html", context)
    
def cart(request):
    context = {}
    return render(request, "eatery/cart.html", context)
    
def checkout(request):
    context = {}
    return render(request, "eatery/checkout.html", context)



    

