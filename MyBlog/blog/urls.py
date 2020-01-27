from django.urls import re_path
from . import views
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap


sitemaps = {
        'posts': PostSitemap,
}


urlpatterns = [
    re_path('list/', views.post_list, name = 'post_list'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/'\
            r'(?P<post>[-\w]+)/',
            views.post_detail,
            name = 'post_detail'),
    re_path(r'^(?P<post_id>\d+)/share/$', views.post_share,
            name='post_share'),
    re_path(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name = 'post_list_by_tag'),
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
]

