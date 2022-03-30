from operator import mod


from django.db import models

# Create your models here.

class Base(models.Model):
    img =  models.FileField(upload_to='static/img')

class Category(models.Model):
    cateimg = models.FileField(upload_to='static')

class Dis(models.Model):
    cashimg = models.FileField(upload_to='static/img')

class Product(models.Model):
    name = models.CharField(max_length=20, null=True)
    price = models.CharField(max_length=20, null=True)
    proimg = models.FileField(upload_to='static')

    def __str__(self):
        return self.name

class Contact(models.Model):
    First_name = models.CharField(max_length=20, null=True)
    Last_name = models.CharField(max_length=20, null=True)
    Address = models.TextField(max_length=50, null=True)
    Email_Address = models.EmailField(max_length=20, null=True)
    Phone = models.CharField(max_length=10, null=True)
    Message = models.TextField(max_length=50, null=True)

    def __str__(self):
        return self.First_name

class logo(models.Model):
    logoimg = models.FileField(upload_to='static')


class order(models.Model):
    email = models.EmailField(max_length=100,null=True)
    count = models.IntegerField(null=True)
    product_1 = models.ForeignKey(Product,on_delete=models.CASCADE)    

class User(models.Model):
    username = models.CharField(max_length=50, null=True)
    Full_Name = models.CharField(max_length=50, null=True)
    Email = models.EmailField(max_length=50, null=True)
    Password = models.CharField(max_length=50, null=True)

class paralex(models.Model):
    parallex = models.FileField(upload_to='static/img')
    