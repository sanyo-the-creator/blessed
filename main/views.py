from django.shortcuts import render
from .models import Products
# Create your views here.
from django.contrib.auth import get_user_model

def home(response):
    try:
            ls =Products.objects.all
           
            User = get_user_model()
            users = User.objects.all()
            print(users)
    except:
            print("nejde")
    if response.method =="POST":
        
        
                
                
        return render(response, "main/home.html", {"ls":ls,"users":users})
    return render(response, "main/home.html", {"ls":ls,"users":users})
def userproducts(response):
           
    return render(response, "main/userproducts.html", {})

def addProducts(response):
           
    return render(response, "main/addProducts.html", {})
