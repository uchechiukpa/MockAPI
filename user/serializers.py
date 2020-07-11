from rest_framework import serializers
from .models import Exprience
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# User = get_user_model()


class Experience_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Exprience
        fields = ['id','experince','url']

class User_Serialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url','id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

