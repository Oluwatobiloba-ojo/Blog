from django.urls import path, include
from . import views
from rest_framework_nested import routers

route = routers.DefaultRouter()
route.register("appBlogs", views.BlogList, "appBlogs")

route = routers.NestedDefaultRouter(route, "appBlogs", lookup="appBlogs")
route.register("posts", views.PostList, "posts")


urlpatterns = [
    path('comments/<int:postId>/', views.comments, name='comment'),
    path('comment/', views.create_comment, name='comment'),
    path('comment_details/<int:pk>/', views.comment_details, name='comment_details'),
    path("", include(route.urls))
]
