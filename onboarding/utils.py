from .models import *
from django.contrib.auth.models import Group


def createEmployee(email,password,username,company,profile):
    # create user
    try:
        user = User.objects.create_user(email=email,password=password,username=username)
        employee = Group.objects.get_by_natural_key(name="employees")
        user.groups.add(employee)
        # create employee
        employee = Employee.objects.create(user=user,company=company,profile=profile)
        return True
    except Exception as e:
        return False

