# Generated by Django 2.1.4 on 2019-01-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190102_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'ToDo'), (1, 'InProgress'), (2, 'Done')]),
        ),
    ]
