
from http.client import HTTPResponse
from django.shortcuts import render
from .models import Products
# Create your views here.
from django.contrib.auth import get_user_model
from django.core.files.storage import FileSystemStorage

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
    if response.method =="POST":
        if response.POST.get("create"):
            name=response.POST.get("name")
            p=Products(name=name)
            p.description = response.POST.get("description")
            p.categories = response.POST.get("category")
            p.size = response.POST.get("size")
            
            img = response.FILES["image"]
            fileSystemStorage=FileSystemStorage()
            fileSystemStorage.save(img.name,img)
            p.image = img.name
            p.checked = False
            p.save()
            response.user.products.add(p)
            

    
    return render(response, "main/addProducts.html", {})
def productLook(response, id):
    pd =Products.objects.get(id=id)
    
    return render(response, "main/productLook.html", {"pd":pd})    