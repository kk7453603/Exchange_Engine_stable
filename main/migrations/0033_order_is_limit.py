# Generated by Django 3.1.7 on 2021-06-29 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20210626_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_limit',
            field=models.BooleanField(default=False),
        ),
    ]