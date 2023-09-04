# Create your views here.
from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app1.models import Student,academics

 
def SignupPage(request):
    if request.method=='POST':
        rollno=request.POST.get('rollno')
        phnno=request.POST.get('phnno')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user=User.objects.create_user(rollno,phnno,pass1)
            my_user.save()
            return redirect('login')
        
    return render (request,'signup.html')
        
@login_required  # Use the login_required decorator to protect the home view
def home(request):
    return render(request, 'home.html')
def LoginPage(request):
    if request.method=='POST':
        rollno=request.POST.get('rollno')
        pass1=request.POST.get('passw')
        user=authenticate(request,username=rollno,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')
   
def comm(request):
    return render(request, 'communc.html')
def event(request):
    return render(request,'events.html')
def info(request):
    logged_in_user = request.user
    try:
        user_student = Student.objects.get(Rollno=logged_in_user.username)
        context = {"details": [user_student]}  
    except Student.DoesNotExist:
        context = {"details": []}  

    return render(request, 'info.html', context)

def contact(request):
    return render(request,'contact.html')
def calen(request):
    return render(request,'calendar.html')
def notify(request):
    return render(request,'notify.html')
def progress(request):
    logged_in_user = request.user
    try:
        user_student = academics.objects.get(rollno=logged_in_user.username)
        context = {"details": [user_student]}  
    except academics.DoesNotExist:
        context = {"details": []}  

    return render(request, 'progress.html', context)
