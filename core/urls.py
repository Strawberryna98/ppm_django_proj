from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.auth import views
from .views import create_post

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    #path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    #path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('create_post', views.create_post, name='create_post'),
    path('followers_list/<int:pk>', views.followers_list, name='followers_list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)