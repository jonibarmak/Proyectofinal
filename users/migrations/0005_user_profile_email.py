# Generated by Django 4.0.6 on 2022-08-25 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_profile_adress_remove_user_profile_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
    ]
