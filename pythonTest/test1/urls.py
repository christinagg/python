# howdy/urls.py
from django.conf.urls import url
from test1 import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^page2/$', views.page2PageView.as_view()),
]