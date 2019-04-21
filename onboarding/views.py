from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.models import Group
from .models import *
from django.http import HttpResponseRedirect
from .utils import *
from django.contrib.auth import authenticate,login
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

@login_required
def companyDetailView(request,id):
    company = Company.objects.get(pk=id)
    return render(request,'companydetail.html',{'company':company})



class EmployeeCreateView(View):

    def get(self,request, id=None):
        print(request.user.username)
        if id:
            form = EmployeeForm()
            form.companyId = id
        else:
            company = request.user.companies.get()
            form = EmployeeForm({'companyId':company.pk})
        return render(request,'employeeregister.html',{'form':form})
    # have a token for invite to increase security
    def post(self,request):
        try:
            email = request.POST['email']
            password = request.POST['password']
            profile = request.POST['profile']
            username = request.POST['username']
            companyId = request.POST['companyId']
            #create employee and add it to the 
            print(companyId)
            createEmployee(email,password,username,companyId,profile)
            if request.user:
                return HttpResponseRedirect('/ob/company/'+str(companyId))
            else:
                return HttpResponseRedirect('/ob/login/')
        except Exception as e:
            print(e)
            return  HttpResponseRedirect('/ob/login')



class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request, 'login.html',{'form':form})
    
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            redirecturl = getRedirectUrl(user)
            login(request,user)
            return HttpResponseRedirect(redirecturl)
        else:
            return HttpResponseRedirect('/ob/login')


@login_required
def employeeDetailView(request,id):
    employee = Employee.objects.get(pk=id)
    return render('employeedetail.html',{'employee':employee})


class EmployeeEditView(View):
    
    def get(self,request,id):
        employee = Employee.objects.get(pk=id)
        form  = EmployEditForm({'profile':employee.profile})
        return render(request,'employeeedit.html',{'form':form,'employee':employee})
    
    def post(self,request,id):
        profile = request.POST['profile']
        employee = Employee.objects.get(pk=id)
        employee.profile = profile
        employee.save()
        redirecturl = getRedirectUrl(request.user)
        return HttpResponseRedirect(redirecturl)
        