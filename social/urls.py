from django.urls import path

from . import views

app_name = 'social'

urlpatterns = []
urlpatterns = [
    path('', views.home, name='home'),
    path('utilizadores/', views.users, name='users'),
    path('utilizadores/<str:username>/', views.user_posts, name='user_posts'),
]
