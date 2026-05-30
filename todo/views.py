
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import signup_model,tasks

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if signup_model.objects.filter(email=email).exists():
            if signup_model.objects.filter(password=password).exists():
                request.session['email'] = email
                return redirect('todo')
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
        
def todo(request):
    if request.method == 'POST':
        user = request.session.get('email')
        task = request.POST['todo']
        
        j = tasks(task_name=task,email=user)
        j.save()
        k = tasks.objects.filter(email=user)
        return render(request, 'html/todopage.html', {'p':k})
    user = request.session.get('email')
    if user:
        k = tasks.objects.filter(email=user)
        return render(request, 'html/todopage.html', {'p':k})

def logout(request):
    request.session.clear()
    return redirect('login')
def delete(request,a):
    s = tasks.objects.get(id=a)
    s.delete()
    return redirect('todo')
def update(request,b):
    user = request.session.get('email')
    if request.method == 'POST':
        
        task = request.POST['todo']
        j = tasks.objects.filter(email=user,id=b).update(task_name=task)
        
        return redirect('todo')
       
    else:
        #k = tasks.objects.all()
        p= tasks.objects.filter(email=user)
        s= tasks.objects.get(email=user, id=b)
       
        return render(request, 'html/update.html', {'p':p,'s':s})


