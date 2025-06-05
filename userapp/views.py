from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html')

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('admin')
        password = request.POST.get('password')
        admin_user = AdminUser.objects.filter(username=username, password=password)
        if admin_user:
            return render(request, 'adminhome.html')
        else:
            error_message = "Invalid username or password"
            return render(request, 'adminlogin.html', {'error': error_message})
    return render(request, 'adminlogin.html')

def adminhome(request):
    return render(request, 'adminhome.html')

def add_teacher(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        idn = request.POST.get('idn')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        address = request.POST.get('address')
        teacher = Teacher.objects.create(teacher_name=name, teacher_id=idn, teacher_subject=subject, teacher_email=email, teacher_address=address)
        teacher.save()
        if teacher:
            return redirect('teachersdetails')
    return render(request, 'add_teacher.html')

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        idn = request.POST.get('idn')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        student = Student.objects.create(student_name=name, student_password=password, student_id=idn, student_email=email, student_phone=phone, student_address=address)
        student.save()
        if student:
            return redirect('studentsdetails')
    return render(request, 'add_student.html')

def teachers_details(request):
    staff = Teacher.objects.all()
    return render(request, 'teachers_detail.html', {'teachers':staff})

def students_details(request):
    student = Student.objects.all()
    return render(request, 'students_detail.html', {'students':student})

def student_delete(request,idn):
    student = Student.objects.get(id=idn)
    student.delete()
    return redirect('studentsdetails')

def teacher_delete(request,idn):
    teacher = Teacher.objects.get(id=idn)
    teacher.delete()
    return redirect('teachersdetails')

def teacher_edit(request,idn):
    teacher = Teacher.objects.filter(id=idn)
    if request.method == 'POST':
        idl = request.POST.get('id')
        name = request.POST.get('name')
        idn = request.POST.get('idn')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        address = request.POST.get('address')
        teacher = Teacher.objects.filter(id=idl)
        teacher.update(teacher_name=name, teacher_id=idn, teacher_subject=subject, teacher_email=email, teacher_address=address)
        if teacher:
            return redirect('teachersdetails')

    return render(request, 'edit_teacher.html', {'teacher':teacher})

def student_edit(request,idn):
    student = Student.objects.filter(id=idn)
    if request.method == 'POST':
        idl = request.POST.get('id')
        name = request.POST.get('name')
        idn = request.POST.get('idn')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        student = Student.objects.filter(id=idl)
        student.update(student_name=name, student_id=idn, student_phone=phone, student_email=email, student_address=address)
        if student:
            return redirect('studentsdetails')
    return render(request, 'edit_student.html', {'student':student})

def logout_view(request):
    logout(request)
    return redirect('index')

def studentlogin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        student = Student.objects.filter(student_name=name, student_password=password)
        if student:
            staff = Teacher.objects.all()
            for data in student:
                request.session['idn']=data.id
                username=data.student_name
            return render(request, 'studenthome.html',{'student':username, 'teachers':staff})
        else:
            return render(request, 'student_login.html', {'message':'Invalid Username or password'})
    return render(request, 'student_login.html')
# Create your views here.
