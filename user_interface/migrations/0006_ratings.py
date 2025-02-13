# Generated by Django 4.1.7 on 2023-04-08 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_interface', '0005_alter_movie_avg_rating_alter_movie_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('rating', models.IntegerField(verbose_name=range(1, 5))),
            ],
        ),
    ]
