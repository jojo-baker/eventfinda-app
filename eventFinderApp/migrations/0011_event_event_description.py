# Generated by Django 2.2 on 2019-09-26 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinderApp', '0010_remove_event_event_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_description',
            field=models.TextField(default='Description', max_length=600),
        ),
    ]
