# Generated by Django 3.2.6 on 2021-10-01 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umm', '0009_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='no',
            new_name='content',
        ),
    ]