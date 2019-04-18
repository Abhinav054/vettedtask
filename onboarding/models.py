from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Company(models.Model):
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=128)


class Employee(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    profile = models.CharField(max_length=128)


class Team(models.Model):
    name = models.CharField(max_length=128)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    employees = models.ManyToManyField(Employee)


