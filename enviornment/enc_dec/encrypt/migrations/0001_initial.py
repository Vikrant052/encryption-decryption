# Generated by Django 5.1.5 on 2025-01-19 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=500, unique=True)),
                ('hashed_data', models.TextField()),
            ],
        ),
    ]
