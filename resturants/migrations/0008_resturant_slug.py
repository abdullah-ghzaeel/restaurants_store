# Generated by Django 3.0.4 on 2021-05-28 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resturants", "0007_auto_20210503_1521"),
    ]

    operations = [
        migrations.AddField(
            model_name="resturant",
            name="slug",
            field=models.SlugField(blank=True, null=True),
        ),
    ]
