"""
URL configuration for keshe2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from library import views as mysql_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('classroom/insert_init',mysql_views.classroom_init),
    # path('classroom/select',mysql_views.classroom_init),

    path('user/select',mysql_views.user_select),
    path('user/register',mysql_views.user_register),
    path('user/login',mysql_views.user_login),
    path('user/update',mysql_views.user_update),
    path('user/delete',mysql_views.user_delete),

    path('reservation/insert',mysql_views.reservation_insert),
    path('reservation/select',mysql_views.reservation_select),
    path('reservation/selectById',mysql_views.reservation_select_by_id),
    path('reservation/update',mysql_views.reservation_update),  
    path('reservation/delete',mysql_views.reservation_delete), 
]
