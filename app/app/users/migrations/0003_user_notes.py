# Generated by Django 3.1.1 on 2021-01-06 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Notes'),
        ),
    ]
