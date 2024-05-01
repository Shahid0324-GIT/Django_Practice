from django.urls import path


from . import views

urlpatterns = [
    path('', views.landing_page, name="home"),
    path("posts/", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail") # /posts/blog-1
]
