# Generated by Django 5.1.3 on 2024-12-14 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_image_characterimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='avatar',
            field=models.TextField(default='https://static-00.iconduck.com/assets.00/avatar-default-symbolic-icon-479x512-n8sg74wg.png'),
        ),
    ]
