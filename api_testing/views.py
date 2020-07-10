from django.shortcuts import render

# Create your views here.
from api_testing.models import User_profiles, Projects
from api_testing.serializers import User_profilesSerializer, ProjectsSerializer
from rest_framework import viewsets


class User_profilesViewSet(viewsets.ModelViewSet):
    queryset = User_profiles.objects.all()
    serializer_class = User_profilesSerializer


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer