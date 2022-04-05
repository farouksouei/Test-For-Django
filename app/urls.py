from django.urls import path
from . import views

urlpatterns = [
    path('posts/', PostsViews.as_view(), name='posts_view'),
]
