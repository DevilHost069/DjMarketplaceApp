# Generated by Django 3.2.6 on 2021-12-31 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0003_auto_20211231_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='listingads',
        ),
    ]
