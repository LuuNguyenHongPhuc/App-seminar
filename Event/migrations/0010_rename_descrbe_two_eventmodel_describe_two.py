# Generated by Django 5.1.4 on 2025-02-04 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0009_rename_id_user_boximage_id_event_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventmodel',
            old_name='descrbe_two',
            new_name='describe_two',
        ),
    ]
