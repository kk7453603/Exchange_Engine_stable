# Generated by Django 3.1.7 on 2021-05-13 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_settings_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='description',
            field=models.IntegerField(default=0),
        ),
    ]
