# Generated by Django 2.1.2 on 2018-10-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perros', '0002_auto_20181028_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Estado',
            field=models.CharField(max_length=10),
        ),
    ]
