# Generated by Django 4.2 on 2025-02-18 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('util', '0004_alter_qrcheckevent_qr_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcheckevent',
            name='email',
            field=models.CharField(default='', max_length=266, null=True),
        ),
    ]
