# Generated by Django 4.1.3 on 2023-02-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0005_imagedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='usercontact',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=25)),
                ('num', models.CharField(max_length=30)),
                ('course', models.CharField(max_length=25)),
            ],
        ),
    ]
