# Generated by Django 5.0.1 on 2024-01-31 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_details',
            old_name='eamil',
            new_name='email',
        ),
    ]
