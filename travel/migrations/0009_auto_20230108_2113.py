# Generated by Django 3.0.3 on 2023-01-08 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0008_auto_20230108_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attractionpost',
            name='attraction_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/attractions'),
        ),
    ]
