from email.policy import default
from statistics import quantiles
from django.contrib.auth.models import User
from django.db import models
from django_mysql.models import ListCharField
# Create your models here.
# me

        
class Products(models.Model):
    user = models.ForeignKey(
         User, on_delete=models.CASCADE, related_name="products", null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    size=models.CharField(max_length=10)
    active=  models.BooleanField(default=True)
    image=models.ImageField(upload_to="", null=True)
    condition=models.CharField(max_length=5,null=True)
    price=models.FloatField(default=0)
    color1=models.CharField(max_length=7,default="#FFFFFF")
    color2=models.CharField(max_length=7,default="#000000")
    categories= models.CharField(max_length=100)
    country= models.CharField(max_length=20)
     #shoes/clothes
    # categories = ListCharField(
    #     base_field=models.CharField(max_length=20),
    #     size=6,
    #     max_length=(500)
    # )
    


    def _str_(self):
        return self.name

class Wanted(models.Model):
    user = models.ForeignKey(
         User, on_delete=models.CASCADE, related_name="wanted", null=True)
    name = models.CharField(max_length=100)
    categories= models.CharField(max_length=100) 
    size=models.CharField(max_length=10)
    active=  models.BooleanField(default=True)
    image=models.ImageField(upload_to="", default="/blessedimg.jpeg")
    maxprice=models.FloatField(default=0)
    color1=models.CharField(max_length=7,default="#FFFFFF")
    color2=models.CharField(max_length=7,default="#000000")
    country= models.CharField(max_length=20)
    
    


    def _str_(self):
        return self.name


























# class Cart(models.Model):
#     user = models.ForeignKey(
#          User, on_delete=models.CASCADE, related_name="cart", null=True)
#     subtotal= models.IntegerField(default=0)
#     def _str_(self):
#         return self.user


# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     productid = models.IntegerField()
#     name = models.CharField(max_length=100, default='SOME STRING')
#     size=models.CharField(max_length=10,default=0)
#     image=models.ImageField(upload_to="", null=True)
#     price=models.FloatField(default=0)
    
#     def _str_(self):
#         return self.productid


# class Orders(models.Model):
#     user = models.ForeignKey(
#          User, on_delete=models.CASCADE, related_name="orders", null=True)
#     name=models.CharField(max_length=100)
#     mail=models.CharField(max_length=100)
#     phone=models.IntegerField()
#     address=models.CharField(max_length=100)
#     payment_method=models.CharField(max_length=100)
#     products = ListCharField(
#          base_field=models.IntegerField(),
#          size=6,
#          max_length=(500)
#      )
#     subtotal=models.IntegerField()
#     date=models.DateField()

   
    
    


    def _str_(self):
        return self.name