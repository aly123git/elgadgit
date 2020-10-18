from django.shortcuts import render, redirect
from django.urls import reverse
from .models import fresh, fresh_ar

#----------------------------------------------------

def fresh_list(request):
    x = fresh.objects.all()
    context={'all_fresh':x}
    return render(request, 'fresh_list.html',context)

#----------------------------------------------------

def fresh_detail(request, id):
    z = fresh.objects.get(id=id)
    return render(request, 'fresh_detail.html', {'one_fresh':z})


def fresh_list_ar(request):
    x = fresh_ar.objects.all()
    context={'all_fresh_ar':x}
    return render(request, 'fresh_list_ar.html',context)

#----------------------------------------------------

def fresh_detail_ar(request, id):
    z = fresh_ar.objects.get(id=id)
    return render(request, 'fresh_detail_ar.html', {'one_fresh':z})



