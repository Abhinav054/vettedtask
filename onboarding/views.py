from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.models import Group
from .models import *
from django.http import HttpResponseRedirect
from .utils import *
# Create your views here.


class CompanyCreateView(View):

    def get(self,request):
        form = CompanyForm()
        return render(request,'companycreate.html',{'form':form})
    def post(self,request):
        try:
            email = request.POST['email']
            password = request.POST['password']
            companyName = request.POST['companyName']
            username = request.POST['username']
            #create user and add it to the companyadmin groups
            user = User.objects.create_user(email=email,password=password,username=username)
            companyadmin = Group.objects.get_by_natural_key(name="company_admins")
            user.groups.add(companyadmin)
            # create company
            company = Company.objects.create(admin=user,company_name=companyName)
            return HttpResponseRedirect('/ob/company/'+str(company.pk))
        except Exception as e:
            print(e)
            return  HttpResponseRedirect('/ob/register/company')



def companyDetailView(request,id):
    company = Company.objects.get(pk=id)
    return render(request,'companydetail.html',{'company':company})



class EmployeeCreateView(View):
    def get(self,request):
        form = EmployeeForm()
        return render(request,'employeeregister.html',{'form':form})
    
    @login_required
    def post(self,request):
        try:
            email = request.POST['email']
            password = request.POST['password']
            profile = request.POST['profile']
            username = request.POST['username']
            company = Company.objects.get(admin=request.user)
            #create user and add it to the companyadmin groups
            return HttpResponseRedirect('/ob/company/'+str(company.pk))
        except Exception as e:
            print(e)
            return  HttpResponseRedirect('/ob/register/company')

