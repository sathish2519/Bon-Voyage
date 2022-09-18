from django.shortcuts import render

# Create your views here.
import email
from imaplib import _Authenticator #auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User #db creation
from django.contrib import messages
from django.contrib.auth import authenticate #authentication
from django.contrib.auth import login  #showing message
def account(request):
    '''
    if request.method=="POST":
        email =request.POST['email']
        password=request.POST['password']

        user= authenticate( email= email ,password =password)

        if user is not None:
            login(request,user)
            return render(request,"auth/dasboard.html")
        else:
            messages.error(request,"Invalid credentials")
            return redirect('account')
            '''
    return render(request,"demo/account.html")

def register(request):
    '''
    if request.method =="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password_confirmation=request.POST['password_confirmation']
        
        #table creation to store values
        myuser=User.objects.create_user(username,email,password) #table
        myuser.password_confirmation= password_confirmation
        myuser.save()

        messages.success(request,"your account has been created")
        return redirect('account')   
'''
    return render(request,"demo/register.html")

def dashboard(request):
    return render(request,"demo/dashboard.html")

def lockscreen(request):
    return render(request,"demo/lockscreen.html")

def restaurant(request):
    return render(request,"demo/restaurant.html")

# Create your views here.
