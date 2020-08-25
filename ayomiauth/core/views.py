from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import login, authenticate 
from ayomiauth.core.forms import SignUpForm, EmailForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.template import RequestContext

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
    current_user = request.user
    if request.method == 'POST':
        Model = get_user_model()
        user = Model.objects.get(email=current_user.email)
        form = EmailForm(request.POST, instance=user)
        if form.is_valid():
            current_user = form.save()
            return render(request, 'my_account.html', {'form': form, 'current_user': current_user })
    else:
        form = EmailForm()
    return render(request, 'my_account.html', {
        'form': form,
        'current_user': current_user,
        })
