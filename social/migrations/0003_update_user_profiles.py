from django.db import migrations


def update_user_profiles(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Profile = apps.get_model('social', 'Profile')

    nathan = User.objects.filter(username='nathan').first()
    if nathan:
        nathan.first_name = 'Nathan'
        nathan.last_name = 'Santos'
        nathan.save(update_fields=['first_name', 'last_name'])
        Profile.objects.update_or_create(
            user=nathan,
            defaults={'bio': 'Aluno de Cybersecurity.'},
        )

    marcio = User.objects.filter(username='maria').first()
    if marcio:
        marcio.username = 'marcio'
        marcio.first_name = 'Marcio'
        marcio.last_name = 'Araujo'
        marcio.email = 'marcio@example.com'
        marcio.save(update_fields=['username', 'first_name', 'last_name', 'email'])
        Profile.objects.update_or_create(
            user=marcio,
            defaults={'bio': 'Aluno de Cybersecurity.'},
        )


def restore_user_profiles(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Profile = apps.get_model('social', 'Profile')

    nathan = User.objects.filter(username='nathan').first()
    if nathan:
        Profile.objects.update_or_create(
            user=nathan,
            defaults={'bio': 'Aluno de administracao de sistemas e desenvolvimento web.'},
        )

    maria = User.objects.filter(username='marcio').first()
    if maria:
        maria.username = 'maria'
        maria.first_name = 'Maria'
        maria.last_name = 'Costa'
        maria.email = 'maria@example.com'
        maria.save(update_fields=['username', 'first_name', 'last_name', 'email'])
        Profile.objects.update_or_create(
            user=maria,
            defaults={'bio': 'Gosta de bases de dados, Linux e cafe forte.'},
        )


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_seed_initial_data'),
    ]

    operations = [
        migrations.RunPython(update_user_profiles, restore_user_profiles),
    ]
