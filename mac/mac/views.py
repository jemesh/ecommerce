from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
def index(request):
    return render(request,'index.html')
def examp(request):
    return render(request,'examp.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
def signupform(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        rpt_password = request.POST['rpt_password']
        if password==rpt_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('/login')
        else:
            messages.info(request,'password should be same')
            return redirect('signup')
    else:
        return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
