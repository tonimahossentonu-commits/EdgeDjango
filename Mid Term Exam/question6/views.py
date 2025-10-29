from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')
