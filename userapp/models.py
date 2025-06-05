from django.db import models

class AdminUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_password = models.CharField(max_length=50)
    student_id = models.CharField(max_length=20)
    student_email = models.EmailField()
    student_phone = models.IntegerField()
    student_address = models.TextField()

    def __str__(self):
        return self.student_name
    
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=20)
    teacher_id = models.CharField(max_length=20)
    teacher_subject = models.CharField(max_length=20)
    teacher_email = models.EmailField()
    teacher_address = models.TextField()


# Create your models here.
