# Generated by Django 4.0.6 on 2024-02-20 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0005_tour_type_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='Itinerary',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
