# Generated by Django 4.0.6 on 2022-07-16 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0005_alter_task_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, through='tasks.TaskLabelRelation', to='labels.label', verbose_name='Метки'),
        ),
    ]