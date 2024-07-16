from django.urls import path
from . import views

app_name = "user_management"

urlpatterns = [
    path("follows/", views.manage_follows, name="manage_follows"),
    path("unfollow/<str:username>/", views.unfollow_user, name="unfollow_user"),
]
