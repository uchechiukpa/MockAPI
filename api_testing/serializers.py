from rest_framework_json_api import serializers
from api_testing.models import User_profiles, Projects


class User_profilesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_profiles
        fields = ('firstname','lastname','country','state','jobtitle','phoneno', 'projects_set')
        # fields = '__all__'

class ProjectsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Projects
        fields = ('title', 'projectdetail','User_profiles')
        # fields = '__all__'
