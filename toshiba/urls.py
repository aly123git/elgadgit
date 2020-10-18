from django.urls import path
from . import views
app_name= 'toshiba'

urlpatterns = [
    path('toshiba_en/', views.toshiba_list, name='toshiba_list'),
    path('toshiba_ar', views.toshiba_list_ar, name='toshiba_list_ar'),

    path('toshiba_en/<int:id>', views.toshiba_detail, name='toshiba_detail'),
    path('toshiba_ar/<int:id>', views.toshiba_detail_ar, name='toshiba_detail_ar'),

]
