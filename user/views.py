from django.shortcuts import render
from rest_framework import viewsets
from . import serializers, models
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from rest_framework.settings import api_settings


# Create your views here.

class ExperinceView(viewsets.ModelViewSet):
    queryset = models.Exprience.objects.all()
    serializer_class = serializers.Experience_Serializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.User_Serialzer
    
class ProfileLoginView(ObtainAuthToken):
    """Handle Creating User auth token """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES #to make it visible


