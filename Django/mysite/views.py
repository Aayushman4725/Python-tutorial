
from django.shortcuts import render
from employees.models import Employee , Student


def home(request):
    employee = Employee.objects.all()
    student = Student.objects.all()
    context ={
        'employee' : employee,
        'student' : student,
    }
    return render(request,'home.html', context)