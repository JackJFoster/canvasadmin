# Generated by Django 3.2.18 on 2023-06-27 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extensions', '0005_extension_confirmation_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='extension',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
