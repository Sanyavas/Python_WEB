# Generated by Django 4.2 on 2023-04-26 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]