# Generated by Django 4.2.1 on 2023-06-07 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tipping', '0016_aflladder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aflladder',
            old_name='clud',
            new_name='club',
        ),
        migrations.RenameField(
            model_name='aflladder',
            old_name='draw',
            new_name='draws',
        ),
        migrations.RenameField(
            model_name='aflladder',
            old_name='lose',
            new_name='losses',
        ),
        migrations.RenameField(
            model_name='aflladder',
            old_name='point',
            new_name='pts',
        ),
    ]
