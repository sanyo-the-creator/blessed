from email.policy import default
from django.contrib.auth.models import User
from django.db import models
from django_mysql.models import ListCharField
# Create your models here.
class Products(models.Model):
    user = models.ForeignKey(
         User, on_delete=models.CASCADE, related_name="products", null=True)
    name = models.CharField(max_length=100,required = True)
    description = models.CharField(max_length=1000,required = False)
    size=models.CharField(max_length=10,required = True)
    checked = models.BooleanField()
    active=  models.BooleanField(default=True)
    image=models.ImageField(upload_to="", null=True,required = True)
    categories= models.CharField(max_length=100,required = True) #shoes/clothes
    # categories = ListCharField(
    #     base_field=models.CharField(max_length=20),
    #     size=6,
    #     max_length=(500)
    # )
    


    def _str_(self):
        return self.name
class Cart(models.Model):
    user = models.ForeignKey(
         User, on_delete=models.CASCADE, related_name="cart", null=True)
    subtotal= models.IntegerField()
    def _str_(self):
        return self.user
class CartItem(models.Model):
    todolist = models.ForeignKey(Cart, on_delete=models.CASCADE)
    productid = models.IntegerField()

    def _str_(self):
        return self.productid
class Orders(models.Model):
    user = models.ForeignKey(
         User, on_delete=models.CASCADE, related_name="orders", null=True)
    name=models.CharField(max_length=100)
    mail=models.CharField(max_length=100)
    phone=models.IntegerField(max_length=10)
    address=models.CharField(max_length=100)
    payment_method=models.CharField(max_length=100)
    products = ListCharField(
         base_field=models.IntegerField(),
         size=6,
         max_length=(500)
     )
    subtotal=models.IntegerField(max_length=10)
    date=models.DateField()

   
    
    


    def _str_(self):
        return self.name