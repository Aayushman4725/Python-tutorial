from django.urls import path
from . import views

app_name = 'employees'
urlpatterns = [
     path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('employee/<int:pk>/',views.employee_detail,name='employee_detail'),
   

]