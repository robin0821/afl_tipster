# Generated by Django 4.2.1 on 2023-06-03 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipping', '0007_tippings_picks'),
    ]

    operations = [
        migrations.AddField(
            model_name='tippings',
            name='ateam',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tippings',
            name='ateam_url',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tippings',
            name='hteam',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tippings',
            name='hteam_url',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tippings',
            name='winner',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]