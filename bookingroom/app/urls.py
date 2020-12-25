from django.urls import path
from .import views, views_staff

urlpatterns = [
    path('',views.index),
    path('staff', views_staff.listStaff , name ='list-staff'),
    path('staff/account-staff-list/infostaff/<pk>', views_staff.infostaff, name='info-staff'),
    path('staff/account-staff-list/create-account-staff',views_staff.createstaff, name='create-staff'),
    path('staff/account-user-list', views_staff.listUser , name ='list-user'),
    path('staff/account-user-list/infouser/<pk>', views_staff.infouser, name='info-user'),
    path('staff/account-user-list/create-account-user', views_staff.createuser, name='create-user'),
    path('staff/statistical', views_staff.statistical, name='statistical'),
]