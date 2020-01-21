from django.shortcuts import render
from django.http import HttpResponse
from .models import ShopItem

def homepage(request):          # will work on the starting webpage
    return render(request, 'home.html')

def userdisplay(request):    
    data = ShopItem.objects.all()   
    # code inside data will return all the items(objects) present in the class ShopItems
    # many more methods are available in documentation like .all(), .filter(), etc.
    # below code will display the content of out template file (index.html)
    return render(request, 'index.html', 
    {'alldata': data})   # (after this visit to templates file)
