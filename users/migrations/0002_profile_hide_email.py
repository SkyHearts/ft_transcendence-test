# Generated by Django 5.0.2 on 2024-02-23 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='hide_email',
            field=models.BooleanField(default=False),
        ),
    ]