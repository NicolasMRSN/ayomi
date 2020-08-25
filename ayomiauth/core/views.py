from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from ayomiauth.core.forms import SignUpForm, EmailForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {
        'form': form
        })

def signin(request):
    render(request, 'registration/login.html')

@login_required
def my_account(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            current_user = request.user
            current_user.email = email
    else:
        form = EmailForm()
    return render(request, 'my_account.html', {
        'form': form
    })