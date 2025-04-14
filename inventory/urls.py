from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns = [
    path('', inventory_list, name='inventory_list'),
     path('inventory_list/', inventory_list, name='inventory_list'), 
    path('order/', create_order, name='create_order'),
    path('report/', usage_report, name='usage_report'),

    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    path('storekeeper/', storekeeper_dashboard, name='storekeeper_dashboard'),
    path('storekeeper/', storekeeper_dashboard, name='storekeeper_dashboard_url'),
    path('add_inventory/', add_inventory, name='add_inventory'),
    path('edit_inventory/<int:item_id>/', edit_inventory, name='edit_inventory'),
    path('delete_inventory/<int:item_id>/', delete_inventory, name='delete_inventory'),
    path('catering_officer/', catering_officer_dashboard, name='catering_officer_dashboard_url'),
    path('catering_officer/', catering_officer_dashboard, name='catering_officer_dashboard'),
    path("catering_officer/add_supplier/", add_supplier, name="add_supplier"),
    path("catering_officer/edit_supplier/<int:supplier_id>/", edit_supplier, name="edit_supplier"),
    path("catering_officer/delete_supplier/<int:supplier_id>/", delete_supplier, name="delete_supplier"),
    # path('assistant_catering_dashboard/', assistant_catering_dashboard, name='assistant_catering_dashboard'),
    path('assistant_catering_officer/', assistant_catering_officer_dashboard, name='assistant_catering_officer_dashboard_url'),
    path('default/', default_dashboard, name='default_dashboard'),
]