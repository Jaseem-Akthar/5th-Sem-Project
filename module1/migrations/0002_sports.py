# Generated by Django 4.1.3 on 2022-12-10 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_sport', models.CharField(max_length=30)),
                ('team_size', models.IntegerField()),
            ],
        ),
    ]