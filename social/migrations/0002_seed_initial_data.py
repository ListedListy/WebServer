from django.db import migrations


def create_initial_data(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Profile = apps.get_model('social', 'Profile')
    Post = apps.get_model('social', 'Post')
    Comment = apps.get_model('social', 'Comment')

    users = [
        {
            'username': 'nathan',
            'first_name': 'Nathan',
            'last_name': 'Santos',
            'bio': 'Aluno de Cybersecurity.',
        },
        {
            'username': 'marcio',
            'first_name': 'Marcio',
            'last_name': 'Araujo',
            'bio': 'Aluno de Cybersecurity.',
        },
    ]

    created_users = {}
    for item in users:
        user, _ = User.objects.get_or_create(
            username=item['username'],
            defaults={
                'first_name': item['first_name'],
                'last_name': item['last_name'],
                'email': f"{item['username']}@example.com",
            },
        )
        Profile.objects.get_or_create(user=user, defaults={'bio': item['bio']})
        created_users[item['username']] = user

    posts = [
        {
            'author': 'nathan',
            'title': 'Primeiro deploy em Django',
            'body': 'Hoje comecei a preparar a aplicacao para correr em ambientes separados.',
            'likes': 8,
            'comments': ['Bom inicio!', 'A estrutura esta clara.'],
        },
        {
            'author': 'marcio',
            'title': 'Docker Compose simplifica tudo',
            'body': 'Um ficheiro bem organizado ajuda a levantar a app e a base de dados rapidamente.',
            'likes': 12,
            'comments': ['Concordo.', 'Muito util para producao.', 'Tambem facilita testes.', 'Boa dica.'],
        },
        {
            'author': 'nathan',
            'title': 'Variaveis de ambiente',
            'body': 'Segredos e configuracoes devem ficar fora do codigo versionado.',
            'likes': 5,
            'comments': ['Essencial para seguranca.'],
        },
    ]

    for item in posts:
        post, _ = Post.objects.get_or_create(
            author=created_users[item['author']],
            title=item['title'],
            defaults={'body': item['body'], 'likes': item['likes']},
        )
        for index, comment_body in enumerate(item['comments'], start=1):
            Comment.objects.get_or_create(
                post=post,
                author_name=f'Visitante {index}',
                body=comment_body,
            )


def delete_initial_data(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.filter(username__in=['nathan', 'marcio']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data, delete_initial_data),
    ]
