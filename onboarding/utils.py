from .models import *
from django.contrib.auth.models import Group


def createEmployee(email,password,username,companyId,profile):
    # create user
    try:
        user = User.objects.create_user(email=email,password=password,username=username)
        employee = Group.objects.get_by_natural_key(name="employees")
        user.groups.add(employee)
        # create employee
        company = Company.objects.get(pk=companyId)
        employee = Employee.objects.create(user=user,company=company,profile=profile)
        return True
    except Exception as e:
        raise e

def getRedirectUrl(user):
    admin = Group.objects.get_by_natural_key(name="superadmin")
    company_admin = Group.objects.get_by_natural_key(name="company_admins")
    employees = Group.objects.get_by_natural_key(name="employees")
    usergroups = user.groups.all()
    if admin in usergroups:
        return ""
    elif company_admin in usergroups:
        company = user.companies.get()
        return "/ob/company/"+str(company.pk)
    elif employees in usergroups:
        employee = user.user.get()
        return "/ob/employee/"+str(employee.pk)
    else:
        return "/ob/login"

def verifyEmployee(user,employee):
    if employee.user.id==user.id:
        return True
    else:
        if user.companies.get().pk==employee.company.pk:
            return True
        else:
            return False