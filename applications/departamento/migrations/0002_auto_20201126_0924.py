# Generated by Django 3.1.3 on 2020-11-26 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='short_name',
            field=models.CharField(max_length=7, unique=True, verbose_name='Nombre corto'),
        ),
    ]
