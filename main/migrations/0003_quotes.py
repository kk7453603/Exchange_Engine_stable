# Generated by Django 3.1.7 on 2021-04-02 00:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_portfolio_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.stocks')),
            ],
        ),
    ]