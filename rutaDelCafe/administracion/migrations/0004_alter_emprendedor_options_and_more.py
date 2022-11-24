# Generated by Django 4.1.3 on 2022-11-08 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_alter_administrador_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emprendedor',
            options={'verbose_name': 'Emprendedor', 'verbose_name_plural': 'Emprendedores'},
        ),
        migrations.AddField(
            model_name='emprendedor',
            name='emprendimientos',
            field=models.ManyToManyField(blank=True, null=True, to='administracion.emprendimiento'),
        ),
    ]
