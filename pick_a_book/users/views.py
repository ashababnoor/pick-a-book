from os import name
from django.shortcuts import render , redirect
from django.urls.conf import path
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.shortcuts import render, get_object_or_404
# Create your views here.

from .forms import *
from .models import *
from django.contrib.auth import logout



def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    return render(request , 'users/login.html')


def  register_view(request):
    return render(request , 'users/register.html')


def verify(request, token):
    try:
        profile_obj = Profile.objects.filter(token = token).first()
        
        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')

    except Exception as e : 
        print(e)
    
    return redirect('/')