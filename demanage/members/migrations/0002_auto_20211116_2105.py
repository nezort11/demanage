# Generated by Django 3.1.13 on 2021-11-16 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="member",
            options={
                "default_permissions": [],
                "ordering": ["join_time"],
                "permissions": [],
                "verbose_name": "Member",
                "verbose_name_plural": "Members",
            },
        ),
    ]
