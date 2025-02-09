# Generated by Django 5.1.4 on 2025-02-04 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0008_alter_eventmodel_events'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boximage',
            old_name='id_user',
            new_name='id_event',
        ),
        migrations.RemoveField(
            model_name='eventmodel',
            name='joiner_one',
        ),
        migrations.RemoveField(
            model_name='eventmodel',
            name='joiner_one_describe',
        ),
        migrations.RemoveField(
            model_name='eventmodel',
            name='joiner_one_thumb_png',
        ),
        migrations.RemoveField(
            model_name='eventmodel',
            name='joiner_three',
        ),
        migrations.RemoveField(
            model_name='eventmodel',
            name='joiner_three_describe',
        ),
        migrations.RemoveField(
            model_name='eventmodel',
            name='joiner_three_thumb_png',
        ),
        migrations.RemoveField(
            model_name='eventmodel',
            name='joiner_two',
        ),
        migrations.RemoveField(
            model_name='eventmodel',
            name='joiner_two_describe',
        ),
        migrations.RemoveField(
            model_name='eventmodel',
            name='joiner_two_thumb_png',
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='descrbe_two',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='describe_one',
            field=models.TextField(null=True),
        ),
    ]
