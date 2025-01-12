# Generated by Django 4.1.7 on 2023-04-03 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_interface', '0004_alter_movie_avg_rating_alter_movie_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='avg_rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(max_length=150),
        ),
    ]
