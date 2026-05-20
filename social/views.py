from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .models import Comment, Post


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


def like_post(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_id)
        post.likes += 1
        post.save(update_fields=['likes'])

    return redirect(request.POST.get('next') or 'social:home')


def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_id)
        author_name = request.POST.get('author_name', '').strip()
        body = request.POST.get('body', '').strip()

        if author_name and body:
            Comment.objects.create(post=post, author_name=author_name, body=body)

    return redirect(request.POST.get('next') or 'social:home')
