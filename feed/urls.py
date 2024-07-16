from django.urls import path
from .views import feed_view, user_posts

app_name = "feed"

urlpatterns = [
    path("", feed_view, name="home"),
    path("posts/", user_posts, name="user_posts"),
]
