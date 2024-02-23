# Generated by Django 5.0.2 on 2024-02-23 05:21

import django.db.models.deletion
import users.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(default='default.jpg', upload_to=users.models.user_directory_path)),
                ('is_online', models.BooleanField(default=False)),
                ('nick_name', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]