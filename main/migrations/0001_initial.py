# Generated by Django 4.2.6 on 2023-10-28 23:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LinkMapping",
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
                ("original_url", models.URLField(max_length=255)),
                ("hash", models.CharField(db_index=True, max_length=15, unique=True)),
                ("creation_date", models.DateTimeField(verbose_name="creation date")),
            ],
        ),
    ]