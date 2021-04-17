# Generated by Django 3.1.7 on 2021-04-09 22:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_merge_20210408_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open', models.FloatField()),
                ('close', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.IntegerField(default=1)),
            ],
        ),
    ]
