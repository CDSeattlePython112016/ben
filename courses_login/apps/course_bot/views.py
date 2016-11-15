from django.shortcuts import render, redirect
from .models import Course, User

def index(request):
    context = {
        'Courses': Course.objects.all(),
    }

    return render(request, 'course_bot/index.html', context)

def add(request):
    course_name = request.POST['name']
    description = request.POST['description']
    Course.objects.create(course_name=course_name, description=description)

    return redirect('index')

def confirm(request, id):
    context = {
        'Course': Course.objects.all().filter(id=id),
    }

    return render(request,'course_bot/destroy.html', context)

def destroy(request, id):
    Course.objects.filter(id=id).delete()
    
    return redirect('index')

def users_courses(request):
    context = {
        'users': User.objects.all(),
        'courses': Course.objects.all()
    }
    return render(request, 'course_bot/user_course.html', context)

def add_user(request):
    user = User.objects.get(id=request.POST['user_id'])
    course = Course.objects.get(id=request.POST['course_id'])
    course.attendee.add(user)
    return redirect('course_bot:add_page')
