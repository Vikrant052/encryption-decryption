# Generated by Django 5.1.5 on 2025-01-19 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encrypt', '0003_userdata_hashed_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawUserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=500, unique=True)),
            ],
        ),
    ]
