# Generated by Django 4.2.1 on 2023-06-07 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipping', '0017_rename_clud_aflladder_club_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aflladder',
            name='logo',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]