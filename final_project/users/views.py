from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import User

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required()
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required()
def get_user_info(request):
    user = request.user
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
    else:
        form = UserInfoForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'model': user.favorite_model})
    return render(request, 'users/about.html', {'form': form})


@login_required()
def chenge(request, user):
    pass
