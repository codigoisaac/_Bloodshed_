from django.db import models
from django.contrib.auth.models import User


class Domain(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    tagline = models.CharField(max_length=200)
    slug = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    domain = models.ForeignKey(
        Domain, on_delete=models.SET_NULL, null=True, related_name="topics"
    )
    contributors = models.ManyToManyField(User)

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    slug = models.CharField(max_length=40, unique=True)
    # participants =

    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)

    body = models.TextField()

    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
