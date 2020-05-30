from django.shortcuts import render
from .models import Feed
from django.shortcuts import redirect

def index(request):
    feeds = Feed.objects.all()
    return render(request, 'feedpage/index.html', {'feeds':feeds})

def new(request):
    return render(request, '/feedpage/new.html/')

def show(request):
    return redirect('/feeds/')

def delete(request):
    return redirect('/feeds/')