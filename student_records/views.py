from django.template.loader import get_template
from django.http import HttpResponse
from .models import Student  # Assuming you have a Student model defined

def student_list(request):
    # Assuming you retrieve the list of students from your database
    students = Student.objects.all()
    # Getting the template
    template = get_template('student_records/student_list.html')
    # Rendering the template with the student data and returning as an HTTP response
    return HttpResponse(template.render({'students': students}, request))

# views.py

from django.shortcuts import render, redirect
from .models import Student, Department

def student_list(request):
    students = Student.objects.all()
    departments = Department.objects.all()
    return render(request, 'student_records/student_list.html', {'students': students, 'departments': departments})

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll_number = request.POST.get('roll_number')
        department_id = request.POST.get('department')
        department = Department.objects.get(pk=department_id)
        student = Student.objects.create(name=name, roll_number=roll_number, department=department)
        student.save()
    return redirect('student_list')

def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect('student_list')

def add_department(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        department = Department.objects.create(name=name)
        department.save()
    return redirect('student_list')

def delete_department(request, department_id):
    department = Department.objects.get(pk=department_id)
    department.delete()
    return redirect('student_list')
