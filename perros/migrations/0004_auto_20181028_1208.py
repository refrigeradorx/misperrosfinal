# Generated by Django 2.1.2 on 2018-10-28 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perros', '0003_auto_20181028_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Estado',
            field=models.CharField(choices=[('1', 'Rescatado'), ('2', 'Disponible'), ('3', 'Adoptado')], default=1, max_length=10),
        ),
    ]
