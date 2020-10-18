from django.shortcuts import render, redirect
from django.urls import reverse
from .models import toshiba, toshiba_ar

#----------------------------------------------------

def toshiba_list(request):
    x = toshiba.objects.all()
    context={'all_toshiba':x}
    return render(request, 'toshiba_list.html',context)

#----------------------------------------------------

def toshiba_detail(request, id):
    z = toshiba.objects.get(id=id)
    return render(request, 'toshiba_detail.html', {'one_toshiba':z})


def toshiba_list_ar(request):
    x = toshiba_ar.objects.all()
    context={'all_toshiba_ar':x}
    return render(request, 'toshiba_list_ar.html',context)

#----------------------------------------------------

def toshiba_detail_ar(request, id):
    z = toshiba_ar.objects.get(id=id)
    return render(request, 'toshiba_detail_ar.html', {'one_toshiba':z})



