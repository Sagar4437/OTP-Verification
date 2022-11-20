from django.shortcuts import render, redirect
from .helper import send_otp_to_phone_number
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return render(request, 'home.html')

def login_view(request):
    if request.POST:
        data = request.POST
        try:
            user = User.objects.get(phone_number=data.get('phone_number'))
        except:
            messages.error(request,"Phone number is not registered. Please enter correct phone_number")
            return render(request, 'login.html')
        if authenticate(phone_number=data.get('phone_number'), password=data.get('password')):
            user.otp = send_otp_to_phone_number(data.get('phone_number'))
            user.save()
            return render(request, 'otp_verification.html')
        else:
            messages.error(request,"Username/password is wrong")
            return render(request, 'login.html')
    
    else:
        return render(request, 'login.html')

def otp_verification(request):
    if request.POST:
        data = request.POST
        try:
            user = User.objects.get(phone_number=data.get('phone_number'))
        except:
            messages.error(request,"Phone number is not registered. Please enter correct phone_number")
            return render(request, 'otp_verification.html')

        print(data)

        if user.otp==data.get('otp'):
            login(request, user)
            messages.success(request,"Login Successfully")
            return redirect(home)
        else:
            messages.error(request,"OTP Failed, Type it correctly")
            return render(request, 'otp_verification.html')
    else:
        return render(request, 'otp_verification.html')

def register(request):
    if request.POST:
        data = request.POST
        phone_number = data.get("phone_number")
        username = data.get("username")
        password = data.get("password")
        
        try:
            user = User.objects.get(phone_number=data.get('phone_number'))
            if user:
                messages.warning(request,"User is alredy registred. Please login here")
                return redirect(login_view)
        except Exception as e:
            user = User.objects.create(phone_number=phone_number, username=username)
            user.set_password(password)
            user.save()
            messages.success(request,"User created successfully. Please login to proceed")
            return redirect(login_view)
    
    return render(request, 'register.html')
