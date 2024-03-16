# Generated by Django 4.1.7 on 2024-02-23 01:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tour.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel', '0005_alter_hotel_overview_alter_hotel_review_rate_and_more'),
        ('tour', '0008_remove_tour_itinerary_alter_tour_itineratys_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='map_link',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='tour',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tour',
            name='overview',
            field=models.TextField(max_length=2000),
        ),
        migrations.CreateModel(
            name='Tour_Review',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rate', models.IntegerField(validators=[tour.models.TourReview.validate_max_value])),
                ('comment', models.CharField(max_length=100)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.tour')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Tour_Booking',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('valid_date_from', models.DateField(default=None)),
                ('valid_date_till', models.DateField(default=None)),
                ('no_of_people_booking', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]
