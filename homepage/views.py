from django.shortcuts import render
from .models import Employee

def home(request):
    employees = Employee.objects.all()
    return render(request, 'homepage/home.html', {'employees': employees})