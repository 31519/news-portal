from django.http.response import HttpResponse
from accounts.models import Account
from accounts.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import Account, UserProfile
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from advertise.models import Advertise
from datetime import datetime
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("2")
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            country = form.cleaned_data["country"]
            state = form.cleaned_data["state"]
            gender = form.cleaned_data["gender"]
            username = email.split('@')[0]
            password = form.cleaned_data["password"]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.save()
            user.country = country
            user.phone_number = phone_number
            user.state = state
            user.gender = gender
            user.is_active = True
            user.save()

            profile = UserProfile()
            profile.user_id = user.id
            profile.images = 'default/default-user.jpg'
            profile.save()

            messages.success (request, f"your account {user.username} has been create successfully")


            return redirect('login')
        else:
            return HttpResponse("hi")

            
    else:
        form = RegistrationForm()
    context = {
        'form':form
    }
    return render(request, 'account/register.html', context)


def dashboard(request):
    today = datetime.now()
    user =  request.user
    adv = Advertise.objects.all().filter(user=user)
    context = {
        'adv':adv,
        'date':today
    }
    return render(request, 'account/dashboard.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')
    return render(request, 'account/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def edit_profile(request):
    return render(request, 'account/edit_profile.html')


@login_required(login_url='login')
def change_password(request):
    return render(request, 'account/change_password.html')







