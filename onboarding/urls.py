from django.urls import path
from .views import *

urlpatterns = [
    path('register/company/',CompanyCreateView.as_view()),
    path('company/<int:id>/',companyDetailView),
    path('register/employee/',EmployeeCreateView.as_view()),
    path('register/employee/<int:id>/',EmployeeCreateView.as_view()),
    path('login',LoginView.as_view()),
    path('employee/<int:id>/',employeeDetailView),
    path('edit/employee/<int:id>/',EmployeeEditView.as_view())
]