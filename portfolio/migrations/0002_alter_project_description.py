# Generated by Django 4.1.4 on 2022-12-12 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.CharField(max_length=700),
        ),
    ]