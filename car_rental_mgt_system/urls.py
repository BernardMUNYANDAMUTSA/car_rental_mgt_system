"""
URL configuration for car_rental_mgt_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from rental_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('record_car/', record_car),
    path('record_driver', record_driver),  
    path('show_driver',show_driver),  
    path('edit_driver/<int:id>', edit_driver),  
    path('update_driver/<int:id>', update_driver),  
    path('destroy_driver/<int:id>', destroy_driver), 
    path('approve_booking/<int:id>', approve_booking),
    path('cancel_booking/<int:id>', cancel_booking),
    path('home_page', home_page,name='home_page'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', login_view, name='login'),
    path('booking/', renting_view, name='booking'),
    path('create_booking/', create_booking, name='create_booking'), 
    path('list_bookings/', booking_view, name='booking_view'),
    
]