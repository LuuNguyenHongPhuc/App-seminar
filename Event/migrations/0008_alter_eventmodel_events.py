# Generated by Django 5.1.4 on 2025-01-31 08:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0007_eventmodel_joiner_one_eventmodel_joiner_one_describe_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='events',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
