from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import fav

def createaccount(request):
    if request.method=='POST':
        username= request.POST['username']
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']
        if password1==password2:
            if(User.objects.filter(username=username).exists()):
                messages.info(request,'Username already exist')
                return render(request,'createaccount.html')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request,'email already exist')
                return render(request,'createaccount.html')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return render(request,'signin.html')
                print('user created')
        else:
            messages.info(request,'password did not matched')
            return render(request,'createaccount.html')
        return redirect('/')
        
    else:
        return render(request,'createaccount.html')

def index(request):
    post=fav.objects.all()
    return render(request,'index.html',{'post':post})
def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username ,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Invalid username and password')
            return redirect('signin')
    else:
        return render(request,'signin.html')
def favourite(request):
    post=fav.objects.all()
    return render(request,'favourite.html',{'post':post})
def chrome(request):
    return render(request,'chrome.html')
def windows(request):
    return render(request,'windows.html')
def google(request):
    post=fav.objects.all()
    return render(request,'google.html',{'post':post})
def microsoft(request):
    post=fav.objects.all()
    return render(request,'microsoft.html',{'post':post})
def youtube(request):
    return render(request,'yotube.html')