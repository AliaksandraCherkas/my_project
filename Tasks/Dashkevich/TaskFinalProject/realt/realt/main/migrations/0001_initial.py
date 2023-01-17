# Generated by Django 4.1.4 on 2023-01-12 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RealtorForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('user_phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('user_mail', models.CharField(max_length=80, verbose_name='E-mail')),
                ('user_comment', models.TextField(verbose_name='Сообщение')),
            ],
        ),
    ]