from django.db import models

# Create your models here.
class admindb(models.Model):
    Name=models.CharField(max_length=50, null=True, blank=True)
    Mobile=models.IntegerField(null=True, blank=True)
    Email=models.CharField(max_length=50, null=True, blank=True)
    Image=models.ImageField(upload_to="profile", null=True, blank=True)
    Username=models.CharField(max_length=50, null=True, blank=True)
    Password=models.CharField(max_length=50, null=True, blank=True)
    Confirm=models.CharField(max_length=50, null=True, blank=True)
class categorydb(models.Model):
    Category_Name=models.CharField(max_length=50,null=True,blank=True)
    Description=models.CharField(max_length=50,null=True,blank=True)
    Category_Image=models.ImageField(upload_to="profile",null=True,blank=True)
class productdb(models.Model):
    Product_Name=models.CharField(max_length=50,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Quantity=models.CharField(max_length=50,null=True,blank=True)
    Product_Description=models.CharField(max_length=50,null=True,blank=True)
    Product_Image=models.ImageField(upload_to="profile",null=True,blank=True)
    Category=models.CharField(max_length=50, null=True, blank=True)
class contactdb(models.Model):
    Cname=models.CharField(max_length=50,null=True,blank=True)
    Cemail=models.EmailField(max_length=50,null=True,blank=True)
    Subject=models.CharField(max_length=50,null=True,blank=True)
    Message=models.CharField(max_length=50,null=True,blank=True)
