from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<str:slug>", views.domain, name="domain"),
    path("<str:domainSlug>/<str:topicSlug>", views.topic, name="topic"),
]
