# Generated by Django 4.0.4 on 2022-06-07 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0004_director_alter_actor_gender_alter_actor_name'),
        ('movies', '0002_movie_create_time_movie_director_movie_update_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='actors.director'),
        ),
    ]