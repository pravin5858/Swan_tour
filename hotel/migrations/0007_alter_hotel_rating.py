# Generated by Django 4.0.6 on 2024-02-23 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_alter_hotel_map_link_alter_hotel_overview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='rating',
            field=models.IntegerField(default=0, null=True),
        ),
    ]