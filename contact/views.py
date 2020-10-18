from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def contact_us(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
    
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ['aly_abosehly@yahoo.com'],
        )

    return render(request, 'contact.html', {})


def contact_ar(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
    
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ['aly_abosehly@yahoo.com'],
        )

    return render(request, 'contact_ar.html', {})
