# Generated by Django 3.1.7 on 2021-08-09 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacation', '0002_auto_20210808_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='inn',
            new_name='name',
        ),
    ]