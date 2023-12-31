# Generated by Django 4.1 on 2023-08-08 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0008_rename_sandpfiftytwoweekchange_stocks_sandp52weekchange"),
    ]

    operations = [
        migrations.CreateModel(
            name="LiveStocks",
            fields=[
                (
                    "id",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("exchange", models.CharField(max_length=10, null=True)),
                ("quoteType", models.IntegerField(max_length=5, null=True)),
                ("price", models.FloatField(max_length=30, null=True)),
                ("timestamp", models.FloatField(max_length=30, null=True)),
                ("marketHours", models.IntegerField(max_length=5, null=True)),
                ("changePercent", models.FloatField(max_length=30, null=True)),
                ("dayVolume", models.FloatField(max_length=30, null=True)),
                ("change", models.FloatField(max_length=30, null=True)),
                ("priceHint", models.IntegerField(max_length=5, null=True)),
            ],
        ),
    ]
