# Generated by Django 3.0.3 on 2023-01-08 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0006_auto_20230107_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attractionpost',
            name='attraction_pic_url',
        ),
        migrations.AddField(
            model_name='attractionpost',
            name='attraction_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/attractions'),
        ),
    ]
