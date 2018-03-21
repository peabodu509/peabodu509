from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.feedback_list, name='feedback_list'),
    url(r'^feedback/(?P<pk>\d+)/$', views.feedback_detail, name='feedback_detail'),
    url(r'^feedback/new/$', views.feedback_new, name='feedback_new'),
]