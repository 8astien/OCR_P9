# Generated by Django 5.0.4 on 2024-07-16 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_management", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userfollows",
            options={"verbose_name": "User Follow", "verbose_name_plural": "User Follows"},
        ),
    ]
