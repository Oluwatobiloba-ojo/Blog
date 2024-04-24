from django.urls import path

from user import views

urlpatterns = [
    path('register/', views.register, name='registration'),
    path('login/', views.login, name='login')
]
