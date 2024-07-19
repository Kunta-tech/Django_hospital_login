from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile
from .forms import UserRegistrationForm, UserProfileForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('home')
    return render(request, 'dashboard.html')

def register(request):
    if request.user.is_authenticated:
        logout(request)

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            profile_form = UserProfileForm(request.POST, instance = user)
        
            if profile_form.is_valid():
                # Create UserProfile instance
                profile_form.save()
                
                return redirect('dashboard')  # Change to your desired success URL
            
            messages.success(request, "Profile not saved!! Try Again.")
        else:
            messages.success(request, "Username or Password didn't match!! Try Again.")
    
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()
    
    return render(request, 'signup.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if request.user.is_authenticated:
                logout(request)
            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(request, "Username or Password didn't match!! Try Again.")
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')