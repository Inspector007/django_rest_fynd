# Generated by Django 3.0.5 on 2020-09-19 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0006_auto_20170206_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImdbRatingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popularity_99', models.FloatField()),
                ('director', models.CharField(max_length=100)),
                ('genre', models.TextField()),
                ('imdb_score', models.FloatField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]