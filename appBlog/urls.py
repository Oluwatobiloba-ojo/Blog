from django.urls import path
from . import views


urlpatterns = [
    path("appBlogs/", views.blogs, name='blogs'),
    path('appBlog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('posts/', views.posts, name='posts'),
    path('post_details/<int:pk>/', views.post_details, name='post_details')
]
