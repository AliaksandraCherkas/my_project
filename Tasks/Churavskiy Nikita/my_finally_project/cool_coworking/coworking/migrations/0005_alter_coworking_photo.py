# Generated by Django 4.1.3 on 2022-12-01 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coworking', '0004_alter_coworking_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coworking',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]