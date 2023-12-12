from django.shortcuts import render, redirect , HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required 
from .models import wandekar
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.template import loader
from django.views.generic import  ListView
from django.template import loader
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request,'home.html')

# def register(request):
#     return render(request,'register.html')

# def login(request):
#     return render(request,'login.html')

def login(request):
    if request.session.has_key('is_logged'):
        return redirect('profile')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user=auth.authenticate(email=email,password=password)


        if user is not None:

            auth.login(request, user)
            request.session['is_logged'] = True
            return redirect('profile')
        else:
            messages.info(request, 'invalid email or password')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request): 
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')
# views.py

# from django.shortcuts import render
from .utils import send_verification_email, generate_verification_code

def register(request):
    if request.method == 'POST':
        # Process signup form data
        # full_name = request.POST['full_name']
        user_name = request.POST['user_name']
        email    = request.POST['email']
        password = request.POST['password']
        dob = request.POST['dob']
        gender = request.POST['gender']


        # do all sanitization
        Wandekar = wandekar(user_name=user_name ,email=email, password=password, dob=dob,
                              gender=gender)
        Wandekar.save()
        messages.success(request, 'Add data Sucessful!')
    return render(request, 'register.html')
    #     # Send verification email to the user

    #     user_email = request.GET['email']  # User's email address
    #     verification_code = generate_verification_code()
    #     send_verification_email(user_email, verification_code)
    #     # Rest of the signup process
    #     # ...

    # return render(request, 'register.html')


# def profile(request):
#     user = request.user

#     context = {
#         "user": user,
#     }

#     return render(request, "profile.html", context)