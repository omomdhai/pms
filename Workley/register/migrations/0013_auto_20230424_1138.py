# Generated by Django 2.0.3 on 2023-04-24 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0012_alter_userprofile_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_userprofile_friends_+', to='register.UserProfile'),
        ),
    ]
