# Generated by Django 4.2.1 on 2023-06-02 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tipping', '0003_alter_aflfixture_ateamid_alter_aflfixture_hteamid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aflfixture',
            old_name='hbehind',
            new_name='hbehinds',
        ),
    ]
