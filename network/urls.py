
from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_posts", views.new_posts, name="new_posts"),
    path("all_posts", views.all_posts, name="all_posts"),
    path("posts", views.posts, name="posts"),
    path("following", views.following, name="following"),
    re_path(r"profile/(?P<other_user_name>[\w]+)$", views.profile, name="profile"),
    re_path(r"profile/(?P<other_user_name>[\w]+)/posts", views.profile_posts, name="profile_posts")
]
