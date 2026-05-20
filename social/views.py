from django.shortcuts import render


SAMPLE_USERS = [
    {
        'username': 'nathan',
        'name': 'Nathan Santos',
        'bio': 'Aluno de administracao de sistemas e desenvolvimento web.',
    },
    {
        'username': 'maria',
        'name': 'Maria Costa',
        'bio': 'Gosta de bases de dados, Linux e cafe forte.',
    },
]

SAMPLE_POSTS = [
    {
        'id': 1,
        'author': SAMPLE_USERS[0],
        'title': 'Primeiro deploy em Django',
        'body': 'Hoje comecei a preparar a aplicacao para correr em ambientes separados.',
        'likes': 8,
        'comments': 2,
    },
    {
        'id': 2,
        'author': SAMPLE_USERS[1],
        'title': 'Docker Compose simplifica tudo',
        'body': 'Um ficheiro bem organizado ajuda a levantar a app e a base de dados rapidamente.',
        'likes': 12,
        'comments': 4,
    },
    {
        'id': 3,
        'author': SAMPLE_USERS[0],
        'title': 'Variaveis de ambiente',
        'body': 'Segredos e configuracoes devem ficar fora do codigo versionado.',
        'likes': 5,
        'comments': 1,
    },
]


def home(request):
    return render(request, 'social/home.html', {'posts': SAMPLE_POSTS})


def users(request):
    return render(request, 'social/users.html', {'users': SAMPLE_USERS})


def user_posts(request, username):
    user = next((item for item in SAMPLE_USERS if item['username'] == username), None)
    posts = [post for post in SAMPLE_POSTS if post['author']['username'] == username]

    return render(
        request,
        'social/user_posts.html',
        {
            'profile': user,
            'posts': posts,
        },
    )
