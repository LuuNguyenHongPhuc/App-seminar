# Generated by Django 5.1.4 on 2025-01-05 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventmodel',
            name='images',
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='img1'),
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='img2'),
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='thumb',
            field=models.ImageField(blank=True, null=True, upload_to='thumb'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
