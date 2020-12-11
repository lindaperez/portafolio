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