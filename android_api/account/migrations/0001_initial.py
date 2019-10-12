# Generated by Django 2.2.4 on 2019-10-11 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('fullname', models.CharField(default='nil', max_length=50)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('home_location', models.TextField(default=0)),
                ('phone_number', models.CharField(default=0, max_length=10, unique=True)),
                ('vehicle_type', models.CharField(default=0, max_length=60)),
                ('vehicle_number', models.CharField(default=0, max_length=30)),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('CO2', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('distance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.CharField(choices=[('OF', 'Offline'), ('ON', 'Online'), ('D', 'Driver'), ('P', 'Passenger')], default='OF', max_length=1)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
            ],
        ),
    ]