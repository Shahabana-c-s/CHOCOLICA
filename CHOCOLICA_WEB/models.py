from django.db import models

# Create your models here.
class customerdetailsdb(models.Model):
    username = models.CharField(max_length=50, null=True, blank=True)
    CEmail = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    CConfirm = models.CharField(max_length=50, null=True, blank=True)
class cart(models.Model):
    user = models.CharField(max_length=50, null=True, blank=True)
    product = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.IntegerField(null=True,blank=True)


