# Generated by Django 3.2.9 on 2022-12-03 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0056_auto_20221203_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firsttimeplan',
            name='title',
            field=models.CharField(choices=[('weekly plan', 'weekly plan'), ('monthly plan', 'monthly plan'), ('quarterly plan', 'quarterly plan'), ('half a year plan', 'half a year plan'), ('a year plan', 'a year plan')], max_length=90),
        ),
    ]
