# Generated by Django 5.1 on 2025-03-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lancamento", "0004_alter_lancamento_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lancamento",
            name="dispesa",
            field=models.CharField(max_length=100, verbose_name="Despesa"),
        ),
    ]
