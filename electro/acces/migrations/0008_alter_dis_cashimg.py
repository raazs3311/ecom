# Generated by Django 4.0.2 on 2022-02-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acces', '0007_alter_base_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dis',
            name='cashimg',
            field=models.FileField(upload_to='static/img'),
        ),
    ]
