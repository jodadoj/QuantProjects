# Generated by Django 4.1 on 2023-07-04 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_crypto_last_updated_forex_last_updated"),
    ]

    operations = [
        migrations.RenameField(
            model_name="stocks",
            old_name="sandPfiftyTwoWeekChange",
            new_name="sandP52WeekChange",
        ),
    ]
