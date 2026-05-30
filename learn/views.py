from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import signup_model

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if signup_model.objects.filter(email=email).exists():
            if signup_model.objects.filter(password=password).exists():
                request.session['email'] = email
                return redirect('welcome')
        else:
            return HttpResponse('something error')
    else:    

        return render(request, 'html/login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

       
        if signup_model.objects.filter(email=email).exists():
            return redirect('sign')
        else:
           
            h = signup_model(
                name=name,
                email=email,
                password=password
            )
            h.save()
            return redirect('login')
    else:        
        return render(request, 'html/signup.html')
        
def welcome(request):
    user = request.session.get('email')
    if user:
        return render(request, 'html/response.html')

def logout(request):
    request.session.clear()
    return redirect('login')
    
    



        

