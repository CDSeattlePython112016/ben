from django.shortcuts import render, redirect

def index(request):
    return render(request, 'd_ninja/index.html')

def ninjas(request):
    context = {
        'mutant': True
    }
    return render(request, 'd_ninja/turtles.html', context)

def color(request, color):
    print "======================"
    context = {
    'color': color,
    'mutant': False
    }
    return render(request, 'd_ninja/turtles.html', context)
