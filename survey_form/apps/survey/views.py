from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'survey/index.html')

def process(request):
    if request.method == 'POST':
        request.session['form_data'] = request.POST
    return redirect('/result')

def result(request):
    return render(request, 'survey/result.html')
