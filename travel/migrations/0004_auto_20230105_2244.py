# Generated by Django 3.0.3 on 2023-01-05 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_auto_20230105_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Non-binary', 'Non-binary')], max_length=100, null=True),
        ),
    ]
