from django.shortcuts import render, redirect
from .models import Course

def index(request):
    context = {
    'Courses': Course.objects.all(),
    }
    return render(request, 'course_bot/index.html', context)

def add(request):
    course_name = request.POST['name']
    description = request.POST['description']
    Course.objects.create(course_name=course_name, description=description)
    return redirect('/')

def confirm(request, id):
    context = {
    'Course': Course.objects.all().filter(id=id),
    }
    return render(request,'course_bot/destroy.html', context)

def destroy(request, id):

    Course.objects.filter(id=id).delete()
    return redirect('/')
