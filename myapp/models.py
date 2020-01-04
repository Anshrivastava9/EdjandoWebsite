from django.db import models

class Data(models.Model):
    name=models.TextField()
    email=models.TextField()
    college=models.TextField()
    branch=models.TextField()
    year=models.TextField()
    mobilenumber=models.TextField()
    department=models.TextField(default='None')

class Company(models.Model):
    companyname=models.TextField()
    email=models.TextField()
    designation=models.TextField()
    address=models.TextField()
    name=models.TextField()
    mobilenumber=models.TextField()  
    department=models.TextField(default='None')  


class Message(models.Model):
    name=models.TextField()
    email=models.TextField()
    subject=models.TextField()
    messaging1=models.TextField()