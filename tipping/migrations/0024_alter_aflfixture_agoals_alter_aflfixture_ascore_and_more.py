# Generated by Django 4.2.1 on 2023-06-09 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipping', '0023_alter_aflfixture_abehinds_alter_aflfixture_hbehinds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aflfixture',
            name='agoals',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='aflfixture',
            name='ascore',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='aflfixture',
            name='hgoals',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='aflfixture',
            name='hscore',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]