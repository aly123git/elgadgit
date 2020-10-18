from django.urls import path, include
from . import views
app_name= 'contact'

urlpatterns = [
    path('', views.contact_us, name='contact_us'),
    path('contact_ar', views.contact_ar, name='contact_ar'),

]
