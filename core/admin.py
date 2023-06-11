from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount

# qui registro i modelli per poterli visualizzare nel pannello di amministrazione
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
