# Generated by Django 3.0.2 on 2020-01-16 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200116_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='budget_currency',
        ),
        migrations.AlterField(
            model_name='project',
            name='budget',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='ProjectDeveloper',
        ),
    ]
