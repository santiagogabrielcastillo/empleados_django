# Generated by Django 3.1.3 on 2020-11-26 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['id'], 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
    ]
