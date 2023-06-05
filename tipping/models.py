from django.db import models

# Create your models here.
class AFLTeams(models.Model):
    id = models.CharField(max_length=20, null=False, blank=False, primary_key=True, unique=True, default=0)
    name = models.CharField(max_length=100, null=True, default='')
    logo = models.CharField(max_length=300, null=True, default='')

class AFLFixture(models.Model):
    id = models.CharField(max_length=20, null=False, primary_key=True, unique=False, default='')
    timestr = models.CharField(max_length=100, null=True, default='')
    winner = models.CharField(max_length=100, null=True, default='')
    unixtime = models.BigIntegerField()
    ateam = models.CharField(max_length=100, null=True, default='')
    complete = models.IntegerField(default=0)
    roundname = models.CharField(max_length=100, null=True, default='')
    hbehinds = models.IntegerField(default=0)
    hteamid = models.ForeignKey(AFLTeams, on_delete=models.CASCADE, to_field='id', related_name='home_team', null=True, blank=True)
    is_final = models.CharField(max_length=100, null=True, default=0)
    hgoals = models.IntegerField(default=0)
    localtime = models.DateTimeField(null=True, blank=True)
    venue = models.CharField(max_length=100, null=True, default='')
    ascore = models.IntegerField(default=0)
    is_grand_final = models.CharField(max_length=100, null=True, default=0)
    winnerteamid = models.ForeignKey(AFLTeams, on_delete=models.CASCADE, to_field='id', related_name='winning_team', null=True, blank=True)
    agoals = models.IntegerField(default=0)
    ateamid = models.ForeignKey(AFLTeams, on_delete=models.CASCADE, to_field='id', related_name='away_team', null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    abehinds = models.IntegerField(default=0)
    updated = models.DateTimeField(null=True, blank=True)
    hscore = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    round = models.IntegerField(default=0)
    tz = models.CharField(max_length=100, null=True, default=0)
    hteam = models.CharField(max_length=100, null=True, default=0)

class tippings(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=True, default='')
    last_name = models.CharField(max_length=100, null=True, default='')
    fixture_id = models.CharField(max_length=100, null=True, default='')
    email = models.CharField(max_length=100, null=True, default='')
    picks = models.CharField(max_length=100, null=True, default='')
    margin = models.IntegerField(default=0)
    margin_diff = models.IntegerField(default=0)
    tips = models.IntegerField(default=0)
    hteam = models.CharField(max_length=100, null=True, blank=True, default='')
    ateam = models.CharField(max_length=100, null=True, blank=True, default='')
    winner = models.CharField(max_length=100, null=True, blank=True, default='')
    hteam_url = models.CharField(max_length=200, null=True, blank=True, default='')
    ateam_url = models.CharField(max_length=200, null=True, blank=True, default='')
    round = models.IntegerField(default=0)
    date = models.DateTimeField(null=True, blank=True)
    venue = models.CharField(max_length=100, null=True, default='')
    status = models.CharField(max_length=20, null=True, default='')
    rank = models.IntegerField(default=0)

class tip_summary(models.Model):
    pass
