from django.conf.urls import  url
from django.urls import include, path
from rest_framework import routers
#from .views import project_collection,project_element
from services import views

#router = routers.DefaultRouter()
#router.register('Element/<int:pk>', views.ProjectViewSet.element())
#router.register('list', views.ProjectList)

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<str:sorted>', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectList.as_view()),
    path('projects/create/', views.ProjectCreate.as_view()),

]

'''
urlpatterns = [

    path('projects/', project_collection,name='post_collection'),

    path('projects/<int:pk>', project_element, name='post_element'),

]
'''