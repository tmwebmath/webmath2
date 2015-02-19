from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def is_teacher(user):
    return user.groups.filter(name='teachers').exists()
    
def is_student(user):
    return user.groups.filter(name='students').exists()
    
# def teacher_required(view):
#     return user_passes_test(login_required(view), is_teacher)

@login_required
def home(request):
    return render(request, 'permission/home.html')

@login_required
@user_passes_test(is_teacher)
def teachers(request):
    return render(request, 'permission/teachers.html')
 
@login_required
@user_passes_test(is_student)
def students(request):
    return render(request, 'permission/students.html')
