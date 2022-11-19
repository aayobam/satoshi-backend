# Generated by Django 3.2.9 on 2022-11-19 16:08

import cms.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0051_auto_20221119_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firsttimeplan',
            name='title',
            field=models.CharField(choices=[('monthly plan', 'monthly plan'), ('quarterly plan', 'quarterly plan'), ('half a year plan', 'half a year plan')], max_length=90, validators=[cms.models.validate_existing_plan]),
        ),
    ]
