# Generated by Django 4.0.6 on 2022-07-28 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Имя')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
        ),
    ]
