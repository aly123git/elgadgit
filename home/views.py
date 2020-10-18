from django.shortcuts import render, redirect
from django.urls import reverse

#----------------------------------------------------

def home(request):
    return render(request, 'home.html',{})


def home_ar(request):
    return render(request, 'home_ar.html',{})
