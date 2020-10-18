from django.shortcuts import render, redirect
from django.urls import reverse
from .models import lg, lg_ar

#----------------------------------------------------

def lg_list(request):
    x = lg.objects.all()
    context={'all_lg':x}
    return render(request, 'lg_list.html',context)

#----------------------------------------------------

def lg_detail(request, id):
    z = lg.objects.get(id=id)
    return render(request, 'lg_detail.html', {'one_lg':z})


def lg_list_ar(request):
    x = lg_ar.objects.all()
    context={'all_lg_ar':x}
    return render(request, 'lg_list_ar.html',context)

#----------------------------------------------------

def lg_detail_ar(request, id):
    z = lg_ar.objects.get(id=id)
    return render(request, 'lg_detail_ar.html', {'one_lg':z})



