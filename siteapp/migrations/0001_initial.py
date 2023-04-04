# Generated by Django 4.0.6 on 2023-04-04 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=4)),
                ('site_incharge', models.CharField(max_length=250)),
                ('contact_details', models.TextField()),
            ],
        ),
    ]
