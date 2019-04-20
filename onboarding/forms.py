from django import forms
from .models import Company

class CompanyForm(forms.Form):
    companyName = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()


class EmployeeForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    profile = forms.CharField(max_length=100)
    companyId = forms.IntegerField(widget=forms.HiddenInput)

class EmployeeFormAdmin(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    profile = forms.CharField(max_length=100)
    companies = forms.ModelChoiceField(queryset=Company.objects.all())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)