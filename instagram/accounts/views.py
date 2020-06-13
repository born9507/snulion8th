from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect

# Create your views here.

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password_confirm']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login (request, user)
            return redirect('/feeds')
    return render(request, 'accounts/signup.html')