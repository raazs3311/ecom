# Generated by Django 4.0.2 on 2022-02-23 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='static')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cateimg', models.FileField(upload_to='static')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=20, null=True)),
                ('Last_name', models.CharField(max_length=20, null=True)),
                ('Address', models.TextField(max_length=50, null=True)),
                ('Email_Address', models.EmailField(max_length=20, null=True)),
                ('Phone', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('price', models.CharField(max_length=20, null=True)),
                ('proimg', models.FileField(upload_to='static')),
            ],
        ),
    ]
