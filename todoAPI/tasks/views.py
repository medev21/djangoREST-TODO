from django.shortcuts import render
from tasks.models import Task
from tasks.serializers import TaskSerializer
from tasks.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from tasks.permissions import IsOwnerOrReadOnly
from rest_framework import renderers

from rest_framework.decorators import detail_route
from rest_framework.response import Response
# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides  'list', 'create', 'retrieve',
    'update', and 'destroy' actions.
    Additionally we also provide an extra 'highlight' action.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        task = self.get_object()
        return Response(task.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions
    this pretty much replaces UserList and UserDetail classes
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
