from django.test import TestCase
from rest_framework.test import APITestCase

from portafolio.models import Project
from datetime import datetime
#TDD

class ProjectCreateTestCase(APITestCase):
    def test_create_project(self):
        initial_count_project = Project.objects.count()
        project_attrs = {
            'title':'New Project',
            'started' : datetime.today(),
            'ended' :datetime.today(),
            'backend' :'Django,Python',
            'frontend' :'Angular,Html,CSS,Javascript',
            'repo_name' :'repo',
            'repo_url' :'github://repo',
        }
        response = self.client.post('/services/projects/new',project_attrs)
        if response.status_code !=201:
            print(response.data)
        actual_count_project=Project.objects.count()
        # checking that it was already added
        self.assertEqual(initial_count_project+1,actual_count_project)
        # checking that it was adding fine
        for attr, expected_value in project_attrs:
            self.assertEqual(response.data[attr]==expected_value)
