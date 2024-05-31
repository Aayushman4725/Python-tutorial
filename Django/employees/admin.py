from django.contrib import admin
from .models import Employee
from .models import Student


admin.site.register(Employee)
admin.site.register(Student)