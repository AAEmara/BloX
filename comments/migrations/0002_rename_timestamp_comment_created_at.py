# Generated by Django 5.2.4 on 2025-07-15 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='timestamp',
            new_name='created_at',
        ),
    ]
