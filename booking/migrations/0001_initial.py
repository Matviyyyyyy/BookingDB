# Generated by Django 5.0.6 on 2024-07-04 16:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('check_in_date', models.DateTimeField()),
                ('check_out_date', models.DateTimeField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
                'ordering': ['booking_date'],
            },
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('position', models.CharField(max_length=256)),
                ('hire_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Employe',
                'verbose_name_plural': 'Employes',
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('type', models.CharField(max_length=256)),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=256)),
                ('date_of_birth', models.DateField()),
                ('role', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('full_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(max_length=256)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.booking')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
                'ordering': ['payment_date'],
            },
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.room'),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.employe')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateField(auto_now_add=True)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('comment', models.TextField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.user')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
                'ordering': ['rating'],
            },
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.user'),
        ),
    ]
