# Generated by Django 4.2 on 2023-04-16 07:25

import api.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', api.models.UserManager()),
            ],
        ),
    ]
