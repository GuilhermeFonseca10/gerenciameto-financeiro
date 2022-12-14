# Generated by Django 3.0 on 2022-12-12 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("categoria", "0001_initial"),
        ("conta", "0001_initial"),
        ("usuario", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lucro",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ganhos", models.CharField(max_length=100)),
                (
                    "valor",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("data", models.DateField()),
                ("categorias", models.ManyToManyField(to="categoria.Categoria")),
                (
                    "conta",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="conta.Conta",
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuario.Usuario",
                    ),
                ),
            ],
            options={
                "ordering": ["-valor", "ganhos"],
            },
        ),
    ]
