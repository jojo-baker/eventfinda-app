# Generated by Django 2.2 on 2019-09-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinderApp', '0008_auto_20190926_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_description',
            field=models.TextField(default='Description', max_length=600),
        ),
    ]
