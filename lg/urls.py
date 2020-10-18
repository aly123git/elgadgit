from django.urls import path
from . import views
app_name= 'lg'

urlpatterns = [
    path('lg_en/', views.lg_list, name='lg_list'),
    path('lg_ar', views.lg_list_ar, name='lg_list_ar'),

    path('lg_en/<int:id>', views.lg_detail, name='lg_detail'),
    path('lg_ar/<int:id>', views.lg_detail_ar, name='lg_detail_ar'),

]
