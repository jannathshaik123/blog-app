
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('home/', views.blog_home, name='blog_home'),
    path('create_post/', views.create_post, name='create_post'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('update_post/<int:id>/', views.update_post, name='update_post'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
    path('update_user/', views.update_user, name='update_user'),
    path('user_profile/', views.user_profile, name='user_profile'),
]