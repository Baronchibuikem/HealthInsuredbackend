# Generated by Django 2.2.7 on 2020-03-06 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_enrollment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planregistration',
            name='reminder_sent',
            field=models.BooleanField(default=False),
        ),
    ]
