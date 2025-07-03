from django.contrib import admin

from .models import Domain, Topic, Message

admin.site.register(Domain)
admin.site.register(Topic)
admin.site.register(Message)
