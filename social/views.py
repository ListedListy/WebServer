from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Post


def home(request):
    posts = Post.objects.select_related('author', 'author__profile').prefetch_related('comments')
    return render(request, 'social/home.html', {'posts': posts})


def users(request):
    users_list = User.objects.select_related('profile').filter(posts__isnull=False).distinct()
    return render(request, 'social/users.html', {'users': users_list})


def user_posts(request, username):
    user = User.objects.select_related('profile').filter(username=username).first()
    posts = Post.objects.filter(author=user).prefetch_related('comments') if user else []

    return render(
        request,
        'social/user_posts.html',
        {
            'profile': user,
            'posts': posts,
        },
    )
