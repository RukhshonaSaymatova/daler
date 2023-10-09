# Generated by Django 4.2.4 on 2023-08-10 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='contact',
        ),
        migrations.AddField(
            model_name='organization',
            name='description',
            field=models.TextField(default='описание...', max_length=50, verbose_name='Описание'),
        ),
    ]