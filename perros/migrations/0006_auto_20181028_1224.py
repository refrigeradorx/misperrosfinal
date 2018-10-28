# Generated by Django 2.1.2 on 2018-10-28 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perros', '0005_auto_20181028_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=10)),
                ('Raza', models.CharField(max_length=100)),
                ('Descripcion', models.CharField(max_length=100)),
                ('Fotografia', models.ImageField(upload_to='media')),
                ('Estado', models.CharField(choices=[('1', 'Rescatado'), ('2', 'Disponible'), ('3', 'Adoptado')], default=1, max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Adopcion',
        ),
    ]