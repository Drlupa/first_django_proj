# Generated by Django 4.0.8 on 2023-09-08 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_category_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='titel',
            new_name='title',
        ),
    ]
