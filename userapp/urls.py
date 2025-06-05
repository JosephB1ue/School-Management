from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('studentsdetails/', views.students_details, name='studentsdetails'),
    path('teachersdetails/', views.teachers_details, name='teachersdetails'),
    path('addstudent/', views.add_student, name='addstudent'),
    path('addteacher/', views.add_teacher, name='addteacher'),
    path('student_delete/<int:idn>/', views.student_delete, name='student_delete'),
    path('teacher_delete/<int:idn>/', views.teacher_delete, name='teacher_delete'),
    path('student_edit/<int:idn>/', views.student_edit, name='student_edit'),
    path('teacher_edit/<int:idn>/', views.teacher_edit, name='teacher_edit'),
    path('logout/', views.logout_view),
    path('studentlogin/', views.studentlogin, name='studentlogin')
]