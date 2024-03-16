# Generated by Django 5.0.2 on 2024-03-10 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0002_bus_seat_alter_bus_bus_company_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourBus',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('bus_number', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
