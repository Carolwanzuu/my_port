# Generated by Django 3.2.6 on 2021-08-11 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carol', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='photo',
            field=models.ImageField(null=True, upload_to='profile/'),
        ),
    ]
