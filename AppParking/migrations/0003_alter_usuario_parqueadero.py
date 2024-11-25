# Generated by Django 4.2.16 on 2024-10-23 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("AppParking", "0002_usuario_direccion_usuario_telefono"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="parqueadero",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="AppParking.parqueadero",
            ),
        ),
    ]