# Generated by Django 2.2.5 on 2019-09-18 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_attendances'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetings',
            name='gas_url',
            field=models.CharField(default='', max_length=255),
        ),
    ]
