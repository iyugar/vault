# Generated by Django 4.1 on 2022-08-11 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0003_booknote"),
    ]

    operations = [
        migrations.AddField(
            model_name="booknote",
            name="subtitle",
            field=models.CharField(default="test", max_length=255),
            preserve_default=False,
        ),
    ]