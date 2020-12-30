from django.shortcuts import render


# Create your views here.

import datetime
from django.http import HttpResponse, HttpResponseNotFound

from .models import Project

# Configuring Generic View Project List
from django.views.generic import ListView

class ProjectList(ListView):
    model = Project

#configuring Generic Detail Project views
from django.views.generic import DetailView

class ProjectDetail(DetailView):
    model = Project
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['project_list'] = Project.objects.all()
        return context

# configuring Generic Edit Project
from django.views.generic import UpdateView
from django.urls import reverse_lazy

class ProjectUpdate(UpdateView):
    model = Project
    fields = ['title','backend','frontend','repo_name','repo_url']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('project_list.html')


# Generic Delete
# Delete a project means delete views and features on Cascade
from django.views.generic import DeleteView

class ProjectDelete(DeleteView):
    model = Project
    template_name_suffix = '_delete'
    success_url = reverse_lazy('project_list.html')


'''------------------------------------------------------------'''
from .models import RelProjectUser

class CollaboratorList(ListView):
    model = RelProjectUser


#configuring Generic Detail Collaborator views
from django.views.generic import DetailView

class CollaboratorDetail(DetailView):
    model = RelProjectUser

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['relprojectuser_list'] = RelProjectUser.objects.all()
        return context

# configuring Generic Edit Collaborator
from django.views.generic import UpdateView
from django.urls import reverse_lazy

class CollaboratorUpdate(UpdateView):
    model = RelProjectUser
    fields = ['id_user','id_project']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('relprojectuser_list.html')


# Generic Delete
# Delete a project means delete views and features on Cascade
from django.views.generic import DeleteView

class CollaboratorDelete(DeleteView):
    model = RelProjectUser
    template_name_suffix = '_delete'

    success_url = reverse_lazy('relprojectuser_list.html')
