# Generated by Django 2.1.2 on 2018-10-19 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sexo',
            field=models.CharField(default='M', max_length=1),
        ),
    ]
