from django.urls import path
from . import views


urlpatterns = [
    path("appBlogs/", views.blogs, name='blogs'),
    path('appBlog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('posts/<int:blogId>', views.posts, name='posts'),
    path('post/', views.create_post, name='post'),
    path('post_details/<int:pk>/', views.post_details, name='post_details'),
    path('comments/<int:postId>', views.comments, name='comment'),
    path('comment/', views.create_comment, name='comment'),
    path('comment_details/<int:pk>', views.comment_details, name='comment_details')
]
