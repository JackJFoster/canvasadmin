# Generated by Django 3.2.23 on 2024-05-10 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_course_programme'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='repeating',
            field=models.BooleanField(default=False, verbose_name='Repeating'),
        ),
    ]
