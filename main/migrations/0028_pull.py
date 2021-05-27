# Generated by Django 3.1.7 on 2021-05-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20210524_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pull',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('price', models.FloatField(default=0)),
                ('count', models.IntegerField(default=0)),
                ('type', models.BooleanField(default=False)),
            ],
        ),
    ]
