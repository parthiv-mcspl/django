# Generated by Django 5.0.7 on 2025-03-02 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='detail',
            field=models.CharField(default='your_default_value', max_length=255),
        ),
    ]
