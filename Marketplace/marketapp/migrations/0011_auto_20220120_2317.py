# Generated by Django 3.2.6 on 2022-01-20 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketapp', '0010_alter_listingimages_listingproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='marketapp.review'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set(),
        ),
    ]