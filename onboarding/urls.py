from django.urls import path
from .views import *

urlpatterns = [
    path('register/company',CompanyCreateView.as_view()),
    path('company/<int:id>',companyDetailView),
]