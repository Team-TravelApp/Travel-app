# Generated by Django 3.0.3 on 2023-01-09 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0006_auto_20230109_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='social_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]