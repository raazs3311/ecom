# Generated by Django 4.0.2 on 2022-02-24 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acces', '0004_rename_cash_dis'),
    ]

    operations = [
        migrations.CreateModel(
            name='logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logoimg', models.FileField(upload_to='static')),
            ],
        ),
    ]