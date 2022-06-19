# Generated by Django 4.0.4 on 2022-06-07 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0003_remove_actor_movies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Name')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=6, verbose_name='Gender')),
                ('age', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='actor',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=6, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(max_length=25, unique=True, verbose_name='Name'),
        ),
    ]
