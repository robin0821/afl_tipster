# Generated by Django 4.2.1 on 2023-06-02 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipping', '0004_rename_hbehind_aflfixture_hbehinds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aflteams',
            name='id',
            field=models.CharField(default=0, max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]