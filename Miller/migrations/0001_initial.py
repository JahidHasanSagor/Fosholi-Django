# Generated by Django 2.2.7 on 2019-11-23 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UpChairman', '0001_initial'),
        ('Farmer', '0001_initial'),
        ('DC', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Miller',
            fields=[
                ('m_id', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('m_name', models.CharField(max_length=50)),
                ('m_phone', models.CharField(max_length=15)),
                ('m_address', models.CharField(max_length=150)),
                ('m_email', models.EmailField(max_length=50, unique=True)),
                ('m_password', models.CharField(max_length=50)),
                ('m_nid_no', models.CharField(max_length=25, unique=True)),
                ('m_license_no', models.CharField(max_length=25)),
                ('stock_capacity_detail', models.CharField(max_length=250)),
                ('season_stock_availability', models.CharField(max_length=250)),
                ('upc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UpChairman.UpChairman')),
            ],
        ),
        migrations.CreateModel(
            name='TradeList',
            fields=[
                ('trade_id', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('purchase_amount', models.IntegerField()),
                ('price_per_unit', models.IntegerField()),
                ('date', models.DateField()),
                ('crop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DC.Crop')),
                ('f_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmer.Farmer')),
                ('m_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Miller.Miller')),
            ],
        ),
    ]