from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^add-post/$', views.AddPostView.as_view()),
]