# School-Management

A Simple Django Web-App implementing features of adding, editing and deleting student details and staff details on the admin's side and a student side which shows a registered student, the teachers available for their subjects, with their contact(email).

Login and Table templates are taken from Codepen, but since the css was not looking desirable, i had to make my own changes in the code here and there, which took more time and as a result the project took a lot longer to complete than i had anticipated.

run the file using the same command on terminal, provided you have all the dependencies installed in your device
'python manage.py runserver' 

create a super user to access the database
'python manage.py createsuperuser'

When trying to login to the admin side on the project, note that:
The admin username is set by default to 'admin' and the password to 'admin12345'
but ofcourse if you want to create a new record to the admin database, you can always create a new superuser and an admin record.

# limitation
The Admin is the only one with the capabiliy to add new students, so the student details must be provided by the admin or known by the student.

