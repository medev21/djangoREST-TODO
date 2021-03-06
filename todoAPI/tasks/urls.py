from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from tasks import views

from tasks.views import TaskViewSet, UserViewSet
from rest_framework import renderers



task_list = TaskViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})

task_detail = TaskViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy'
})

task-highlight = TaskViewSet.as_view({
    'get' : 'highlight'
}, renderer_classes = [renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get' : 'list'
})

user_detail = UserViewSet.as_view({
    'get' : 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^snippets/$', snippet_list, name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
])


# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
