# Generated by Django 3.1.7 on 2021-08-07 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
                ('inn', models.CharField(max_length=64)),
                ('room', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('countries', models.ManyToManyField(blank=True, related_name='passengers', to='vacation.Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=240)),
                ('time_posted', models.DateTimeField(auto_now_add=True)),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writer', to='vacation.hotel')),
                ('hotels_liked', models.ManyToManyField(blank=True, related_name='liked_writer', to='vacation.Hotel')),
            ],
        ),
    ]