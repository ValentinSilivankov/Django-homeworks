# Generated by Django 4.2.2 on 2023-06-09 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sensor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30, verbose_name="Название")),
                (
                    "description",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Описание"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Measurement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "temperature",
                    models.FloatField(verbose_name="Температура при измерении"),
                ),
                (
                    "measurement_time",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время измерения"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="",
                        verbose_name="Снимок датчика",
                    ),
                ),
                (
                    "sensor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="measurements",
                        to="measurement.sensor",
                    ),
                ),
            ],
        ),
    ]
