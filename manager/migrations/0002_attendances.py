# Generated by Django 2.2.1 on 2019-05-14 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mtg_id', models.CharField(max_length=255)),
                ('login_name', models.CharField(max_length=255)),
                ('attend', models.BooleanField()),
            ],
        ),
    ]
