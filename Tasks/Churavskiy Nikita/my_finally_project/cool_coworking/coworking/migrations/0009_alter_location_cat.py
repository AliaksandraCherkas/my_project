# Generated by Django 4.1.3 on 2022-12-08 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coworking', '0008_remove_location_connect_location_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tomato', to='coworking.cities'),
        ),
    ]