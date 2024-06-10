from email.policy import default
from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime,timedelta
from django.contrib.auth.models import User,auth
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)

class members(models.Model):
    MID=models.TextField(blank=True)
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    Address=models.CharField(max_length=200)
    Photo=models.ImageField(null=True,blank=True,upload_to='image/')
    email=models.CharField(max_length=255)
    dob=models.CharField(max_length=255)
    phone=models.IntegerField()
    

class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)

class Book(models.Model):
    Name=models.TextField(blank=True)
    Author=models.CharField(max_length=255)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    available=models.BooleanField(default=True)
    stock=models.IntegerField()
    desc=models.CharField(max_length=255)
    year=models.IntegerField()
    language=models.CharField(max_length=255)
    price=models.IntegerField()
    status=models.CharField(max_length=255)
    Photo=models.ImageField(null=True,blank=True,upload_to='image/')

def expiry():
    return datetime.today() + timedelta(days=15)




class Issue(models.Model): 
    usr=models.ForeignKey(members,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    issuedate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=expiry)
    status=models.CharField(max_length=255,default=1)
    fine=models.IntegerField(default=0)
    penalty=models.IntegerField(default=0,blank=True)
    reason=models.TextField(blank=True)
    total=models.IntegerField(blank=True,default=0)





    