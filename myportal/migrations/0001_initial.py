# Generated by Django 2.2.5 on 2019-09-18 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredBrowser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bwid', models.CharField(max_length=255)),
            ],
        ),
    ]
