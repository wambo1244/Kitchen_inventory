from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
     path('inventory_list/', views.inventory_list, name='inventory_list'), 
    path('order/', views.create_order, name='create_order'),
    path('report/', views.usage_report, name='usage_report'),

    path('login/', views.user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    path('storekeeper/', views.storekeeper_dashboard, name='storekeeper_dashboard_url'),
    path('catering_officer/', views.catering_officer_dashboard, name='catering_officer_dashboard_url'),
    path('assistant_catering_officer/', views.assistant_catering_officer_dashboard, name='assistant_catering_officer_dashboard_url'),
    path('default/', views.default_dashboard, name='default_dashboard'),
]
