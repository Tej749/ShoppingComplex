# Generated by Django 5.1 on 2024-08-24 11:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hotel",
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
                ("name", models.CharField(max_length=50)),
                ("loc", models.CharField(max_length=50)),
                ("mob", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=254)),
            ],
            options={
                "db_table": "hotel",
            },
        ),
    ]
