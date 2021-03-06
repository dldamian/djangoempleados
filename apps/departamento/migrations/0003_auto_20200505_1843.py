# Generated by Django 3.0.6 on 2020-05-05 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_auto_20200505_1639'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['nombre'], 'verbose_name': 'Mi Departamento', 'verbose_name_plural': 'Áreas de la Empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('nombre', 'nombre_corto')},
        ),
    ]
