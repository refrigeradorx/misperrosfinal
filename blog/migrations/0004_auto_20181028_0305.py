# Generated by Django 2.1.2 on 2018-10-28 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181023_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=10)),
                ('Raza', models.CharField(max_length=100)),
                ('Descripcion', models.CharField(max_length=100)),
                ('Fotografia', models.ImageField(upload_to='')),
                ('Estado', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='ciudad',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='fecNac',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='nomCompleto',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='region',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='rut',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='telefono',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='vivienda',
            field=models.CharField(max_length=30),
        ),
    ]
