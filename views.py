from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib import messages


# Create your views here.
def registration(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'user has been created successfully ? {username}')
            return redirect('userapp_login')
        else:
            UserRegistrationForm()

    return render(request, 'userapp/registration.html', {'form': form})


def home(request):
    return render(request, 'userapp/home.html', {})