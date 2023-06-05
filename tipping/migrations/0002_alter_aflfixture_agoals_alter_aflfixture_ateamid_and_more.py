# Generated by Django 4.2.1 on 2023-06-02 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tipping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aflfixture',
            name='agoals',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='aflfixture',
            name='ateamid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='tipping.aflteams'),
        ),
        migrations.AlterField(
            model_name='aflfixture',
            name='winnerteamid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winning_team', to='tipping.aflteams'),
        ),
    ]
