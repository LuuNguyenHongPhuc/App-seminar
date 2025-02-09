# Generated by Django 5.1.4 on 2025-01-27 14:07

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoxImage',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='event/')),
            ],
        ),
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('f9394a17-0352-4aa0-88f7-cc33df444f50'), primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(default='', max_length=100)),
                ('describe', models.TextField(default='')),
                ('type', models.CharField(default='', max_length=26)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateField()),
                ('thumb', models.ImageField(upload_to='thumb/')),
                ('end_time', models.DateField()),
                ('author', models.CharField(max_length=266)),
                ('price', models.IntegerField(default=0)),
                ('locate', models.CharField(max_length=266)),
                ('address', models.CharField(max_length=266)),
                ('qr_code', models.ImageField(upload_to='qr-code/')),
                ('facebook_link', models.CharField(max_length=266)),
                ('instagram_link', models.CharField(max_length=266)),
                ('phone', models.CharField(max_length=266)),
                ('max_join', models.IntegerField(default=0)),
                ('current_join', models.IntegerField(default=0)),
            ],
        ),
    ]
