from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^home/$', views.index, name='index'),
	url(r'^post/(?P<slug>[-\w]+)/$', views.post, name="post"),
]