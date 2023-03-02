# Generated by Django 3.2.17 on 2023-02-03 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_assignment_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='graded',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='not_submitted',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='ungraded',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]