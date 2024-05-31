from django.shortcuts import render
from django.shortcuts import get_object_or_404
from employees.models import Employee, Student

# Create your views here.

def employee_detail(request, pk):
    employee = get_object_or_404(Employee,pk=pk)
    context ={
        'employee' : employee,
    }
    return render(request, 'employee_detail.html',context)

def student_detail(request, pk):
    student = get_object_or_404(Student,pk=pk)
    context= {
        'student' : student,
    }
    return render(request, 'student_detail.html',context)