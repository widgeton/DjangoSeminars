"""
URL configuration for project project.

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
from django.urls import path, include
from seminar3.views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('app1/', include('seminar1_app1.urls')),
    path('app2/', include('seminar1_app2.urls')),
    path('app3/', include('seminar3.urls')),
    path('app4/', include('seminar4.urls')),
]
