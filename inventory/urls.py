from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import (
    user_login, storekeeper_dashboard,
    catering_officer_dashboard, assistant_catering_officer_dashboard,
    default_dashboard
)

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
     path('inventory_list/', views.inventory_list, name='inventory_list'), 
    path('order/', views.create_order, name='create_order'),
    path('report/', views.usage_report, name='usage_report'),
    path('login/', views.user_login, name='login'),
    path('storekeeper/', storekeeper_dashboard, name='storekeeper_dashboard'),
    path('catering_officer/', catering_officer_dashboard, name='catering_officer_dashboard'),
    path('assistant_catering_officer/', assistant_catering_officer_dashboard, name='assistant_catering_officer_dashboard'),
    path('default/', default_dashboard, name='default_dashboard'),
]
