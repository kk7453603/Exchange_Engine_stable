# Generated by Django 3.1.7 on 2021-05-27 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_pull'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_limit',
            field=models.BooleanField(default=False),
        ),
    ]
