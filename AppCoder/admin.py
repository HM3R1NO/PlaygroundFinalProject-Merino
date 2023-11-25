from django.contrib import admin
from .models import UserExtension, Chat, Mensaje, Post

admin.site.register(UserExtension)
admin.site.register(Chat)
admin.site.register(Mensaje)
admin.site.register(Post)