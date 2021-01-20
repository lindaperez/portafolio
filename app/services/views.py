from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProjectSerializer
from .forms import ProjectForm
from rest_framework import status

from rest_framework import viewsets,permissions,generics
from .serializers import ProjectSerializer
from portafolio.models import Project




'''
def home(request):
    tmpl_vars = {'form': ProjectForm()}
    return render(request, 'services/index.html', tmpl_vars)



@api_view(['GET'])
def project_element(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def project_collection(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {'title': request.DATA.get('title'), 'id': request.user.pk}
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
'''

#Generic Views RESTful API


#Generic GET
class ProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    queryset = None

    def get(self,request, pk=None, sorted=False):
        if pk:
            self.queryset = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(self.queryset, many=False)
        else:
            if sorted:
                self.queryset = Project.objects.order_by('title')
                serializer = ProjectSerializer(self.queryset, many=True)
            else:
                self.queryset = Project.objects.all()
                serializer = ProjectSerializer(self.queryset, many=True)

        return Response(serializer.data)

class ProjectCreate(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    queryset = None

    def post(self,request):
        serializer = ProjectSerializer(None, many=False)
        return Response(serializer.data)


