# Generated by Django 3.2.20 on 2023-09-25 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20230905_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]