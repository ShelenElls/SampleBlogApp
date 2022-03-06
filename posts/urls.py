from django.urls import path

from posts.views import list_all_posts, show_post_detail

urlpatterns = [
    path("<int:pk>/", show_post_detail, name="post_detail"),
    path("", list_all_posts, name="post_list"),
]
