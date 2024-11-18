# Generated by Django 5.0.6 on 2024-11-17 15:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("lat", models.FloatField()),
                ("lng", models.FloatField()),
                ("isDefault", models.BooleanField(default=False)),
                ("address", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=100)),
                (
                    "addressType",
                    models.CharField(
                        choices=[
                            ("Home", "Home"),
                            ("Ofiice", "Office"),
                            ("Scholl", "School"),
                        ],
                        default="Home",
                        max_length=10,
                    ),
                ),
                (
                    "userId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Extras",
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
                ("isVerified", models.BooleanField(default=False)),
                ("otp", models.CharField(default="", max_length=8)),
                (
                    "userId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
