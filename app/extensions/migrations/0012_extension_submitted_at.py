# Generated by Django 3.2.22 on 2023-11-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extensions', '0011_extension_confirm_self_certified'),
    ]

    operations = [
        migrations.AddField(
            model_name='extension',
            name='submitted_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
