# Generated by Django 3.2.9 on 2021-11-18 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idType', models.CharField(max_length=100)),
                ('idNum', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]