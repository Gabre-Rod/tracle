# Generated by Django 3.0.7 on 2022-01-01 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0026_chunkedvideoupload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='transcoded_video',
        ),
    ]
