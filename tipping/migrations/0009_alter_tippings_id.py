# Generated by Django 4.2.1 on 2023-06-03 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipping', '0008_tippings_ateam_tippings_ateam_url_tippings_hteam_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tippings',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
