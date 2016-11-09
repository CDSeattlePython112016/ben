from django.shortcuts import render, HttpResponse, redirect
import random, string
def index(request):
    return render(request, "randomword/index.html")

def generate(request):
    request.session['attempt'] += 1
    request.session['word'] = ''.join(random.sample(string.lowercase+string.digits,14))
    return redirect('/')
