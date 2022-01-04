# Generated by Django 3.2.6 on 2022-01-03 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketapp', '0006_auto_20220103_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listingimages',
            name='listingproducts',
        ),
        migrations.AddField(
            model_name='listingproducts',
            name='listingimages',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='marketapp.listingimages'),
        ),
    ]