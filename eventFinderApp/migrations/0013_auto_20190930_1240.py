# Generated by Django 2.2 on 2019-09-30 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinderApp', '0012_event_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(default='media/download.jpg', upload_to='event_images/%Y/%m/%D/'),
            preserve_default=False,
        ),
    ]
