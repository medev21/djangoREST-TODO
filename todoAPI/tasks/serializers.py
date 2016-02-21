from rest_framework import serializers
from tasks.models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name = "task-highlight", format = "html")

    class Meta:
        model = Task
        fields = ('url','highlight', 'owner', 'title', 'description')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(many = True, view_name = 'task-detail', read_only = True)

    class Meta:
        model = User
        fields = ('id', 'username', 'tasks')
