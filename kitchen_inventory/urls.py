"""
URL configuration for kitchen_inventory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),


    # path('', views.home, name='home'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('login/', views.user_login, name='login'),
    # path('', views.inventory_list, name='inventory_list'),
    # path('storekeeper/dashboard/', views.storekeeper_dashboard, name='storekeeper_dashboard'),
    # path('assistant-catering-officer/dashboard/', views.assistant_catering_officer_dashboard, name='assistant_catering_officer_dashboard'),
    # path('catering-officer/dashboard/', views.catering_officer_dashboard, name='catering_officer_dashboard'),

]
