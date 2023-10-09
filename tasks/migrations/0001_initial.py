# Generated by Django 4.2.4 on 2023-08-10 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0002_rename_expiry_dt_project_end_dt_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Название задачи')),
                ('description', models.TextField(default='описание...', max_length=50, verbose_name='Описание задачи')),
                ('status', models.CharField(choices=[(' В ожидании', 'Pending'), ('Выполнена', 'Completed'), ('В процессе', 'In Progress'), ('Отменено', 'Canceled')], default=' В ожидании', max_length=20, verbose_name='Статус')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
