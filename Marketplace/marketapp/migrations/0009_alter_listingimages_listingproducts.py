# Generated by Django 3.2.6 on 2022-01-15 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketapp', '0008_auto_20220103_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingimages',
            name='listingproducts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listimg', to='marketapp.listingproducts'),
        ),
    ]