# Generated by Django 4.1.3 on 2022-12-06 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_rol_rename_producto_emprendimiento_productos_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emprendimiento',
            old_name='nombreEmprendiento',
            new_name='nombreEmprendimiento',
        ),
    ]
