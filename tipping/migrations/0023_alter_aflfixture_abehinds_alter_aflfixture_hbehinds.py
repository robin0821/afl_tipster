# Generated by Django 4.2.1 on 2023-06-09 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipping', '0022_tip_ladder_rounds_tipped'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aflfixture',
            name='abehinds',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='aflfixture',
            name='hbehinds',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]