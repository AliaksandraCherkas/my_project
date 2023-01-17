# Generated by Django 4.1.5 on 2023-01-15 19:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_mymodel_remove_post_author_delete_author_delete_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mymodel',
            old_name='content',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='mymodel',
            old_name='kid_name',
            new_name='name_of_kid',
        ),
        migrations.RemoveField(
            model_name='mymodel',
            name='clss_choise',
        ),
        migrations.AddField(
            model_name='mymodel',
            name='class_choice',
            field=models.CharField(choices=[('U', ' Unity game development class'), ('W', ' Web development class'), ('P', ' Python programming class')], default='U', max_length=4),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='phone',
            field=models.CharField(max_length=16, null=True, validators=[django.core.validators.RegexValidator(message="Phone must be entered in format '+123456789'", regex='^\\+\\d{9,15}$')]),
        ),
    ]
