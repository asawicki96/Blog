
from django.urls import re_path
from . import views

urlpatterns = [
    re_path('list/', views.PostListView.as_view(), name = 'post_list'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/'\
            r'(?P<post>[-\w]+)/',
            views.post_detail,
            name = 'post_detail'),
    re_path(r'^(?P<post_id>\d+)/share/$', views.post_share,
            name='post_share'),
]

