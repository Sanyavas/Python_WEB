# Generated by Django 4.2 on 2023-06-01 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0005_quote_user_tag_user_tag_tag_of_username'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='tag',
            name='tag of username',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='user',
        ),
    ]
