# Generated by Django 4.0.2 on 2022-03-03 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acces', '0010_user_confirm_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Confirm_Password',
        ),
    ]
