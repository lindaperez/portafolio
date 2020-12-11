"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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


# configuring generic View ProjectList
from django.urls import path
from .views import ProjectList
from .views import ProjectDetail
from .views import ProjectUpdate

urlpatterns = [
    path('projects/', ProjectList.as_view(),name='project_list.html'),
    path('projects/<int:pk>', ProjectDetail.as_view(), name='project_detail.html'),
    path('projects/edit/<int:pk>', ProjectUpdate.as_view(), name='project_update.html'),

    ]
