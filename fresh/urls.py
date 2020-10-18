from django.urls import path
from . import views
app_name= 'fresh'

urlpatterns = [
    path('fresh_en/', views.fresh_list, name='fresh_list'),
    path('fresh_ar', views.fresh_list_ar, name='fresh_list_ar'),

    path('fresh_en/<int:id>', views.fresh_detail, name='fresh_detail'),
    path('fresh_ar/<int:id>', views.fresh_detail_ar, name='fresh_detail_ar'),

]
