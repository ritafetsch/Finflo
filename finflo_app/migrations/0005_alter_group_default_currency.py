# Generated by Django 4.2.4 on 2023-08-31 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("finflo_app", "0004_group_default_currency"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="default_currency",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="finflo_app.currency",
            ),
        ),
    ]
