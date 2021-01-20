from django import forms
from portafolio.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['repo_name','repo_url','ended', 'backed','frontend','started']
        fields = ['id', 'title' ]
        widgets = {
            'title': forms.TextInput(
                attrs={'id': 'project-text', 'required': True, 'placeholder': 'Project Tittle'}
            )
        }

