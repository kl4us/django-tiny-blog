from django.conf.urls import url

from .views import PostDetailView, PostListView

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post-detail'),
    url(r'^$', PostListView.as_view(), name='post-list'),
]