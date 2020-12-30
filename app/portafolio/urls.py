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
from .views import ProjectDelete

from .views import CollaboratorList
from .views import CollaboratorDetail
from .views import CollaboratorUpdate
from .views import CollaboratorDelete

urlpatterns = [
    path('projects/', ProjectList.as_view(),name='project_list.html'),
    path('projects/<int:pk>', ProjectDetail.as_view(), name='project_detail.html'),
    path('projects/edit/<int:pk>', ProjectUpdate.as_view(), name='project_update.html'),
    path('projects/delete/<int:pk>', ProjectDelete.as_view()),

    path('projects/collaborators/', CollaboratorList.as_view(),name='relprojectuser_list.html'),
    path('projects/collaborators/<int:pk>', CollaboratorDetail.as_view(), name='relprojectuser_detail.html'),
    path('projects/collaborators/edit/<int:pk>', CollaboratorUpdate.as_view(), name='relprojectuser_update.html'),
    path('projects/collaborators/delete/<int:pk>', CollaboratorDelete.as_view()),
    ]
