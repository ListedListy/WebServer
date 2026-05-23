from django.urls import path

from . import views

app_name = 'social'

urlpatterns = [
    path('', views.home, name='home'),
    path('publicacoes/', views.posts, name='posts'),
    path('utilizadores/', views.users, name='users'),
    path('utilizadores/<str:username>/', views.user_posts, name='user_posts'),
    path('publicacoes/<int:post_id>/like/', views.like_post, name='like_post'),
    path('publicacoes/<int:post_id>/comentar/', views.add_comment, name='add_comment'),
]
