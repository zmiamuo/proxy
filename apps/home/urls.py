# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from apps.home import views 


urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('home/notifications.html', views.generate_notification,name="generate_notification"),
    path('home/user.html', views.updateuser, name='updateuser'),
    path('/getLogs', views.getLogs,name="getLogs"),
    
    

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
