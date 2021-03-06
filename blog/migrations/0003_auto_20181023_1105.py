# Generated by Django 2.1.2 on 2018-10-23 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_sexo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='fecNac',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='ciudad',
            field=models.CharField(default='a', max_length=30),
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.CharField(default='a', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='nomCompleto',
            field=models.CharField(default='a', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='region',
            field=models.CharField(default='a', max_length=30),
        ),
        migrations.AddField(
            model_name='post',
            name='rut',
            field=models.CharField(default='a', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='telefono',
            field=models.CharField(default='a', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='vivienda',
            field=models.CharField(default='a', max_length=30),
        ),
    ]
