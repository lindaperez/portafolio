from portafolio.models import Project
from rest_framework import serializers

class ProjectSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'title', 'started')
