# Generated by Django 5.1.5 on 2025-01-20 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encrypt', '0006_alter_userdata_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawuserdata',
            name='email',
            field=models.EmailField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
