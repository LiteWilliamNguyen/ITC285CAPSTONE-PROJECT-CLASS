from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    productname=models.CharField(max_length= 255)
    productdescription=models.TextField(null=True, blank=True)
    productusage=models.TextField(null=True, blank=True)
    productquantity=models.IntegerField()
    user=models.ForeignKey(User, on_delete = models.DO_NOTHING)
    productcost=models.IntegerField()

    def __str__(self):
        return self.productname
    
    class Meta:
        db_table = 'Product'

class Monk(models.Model):
    monkname=models.CharField(max_length= 255)
    monkage=models.IntegerField()
    user=models.ManyToManyField(User)

    def __str__(self):
        return self.monkname
    
    class Meta:
        db_table = 'Monk'
    
class Member(models.Model):
    membername=models.CharField(max_length= 255)
    memberage=models.IntegerField()
    user=models.ManyToManyField(User)
    memberaddress=models.CharField(max_length=255)
    membercity=models.CharField(max_length=50)
    memberstate=models.CharField(max_length=2)
    memberzip=models.IntegerField(max_length=5)
    memberphone=models.IntegerField(max_length=11)

    def __str__(self):
        return self. membername
    
    class Meta:
        db_table = 'Member'


