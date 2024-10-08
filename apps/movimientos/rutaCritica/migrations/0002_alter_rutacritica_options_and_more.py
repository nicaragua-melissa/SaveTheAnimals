# Generated by Django 4.2 on 2024-09-11 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("nivelRuta", "0002_alter_nivelruta_options"),
        ("rutaCritica", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="rutacritica",
            options={"verbose_name_plural": "Rutas Críticas"},
        ),
        migrations.AlterField(
            model_name="rutacritica",
            name="nivelRuta",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="nivelRuta.nivelruta",
                verbose_name="Nivel de Ruta",
            ),
        ),
    ]
