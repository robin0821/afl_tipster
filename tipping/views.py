from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import get_user_model
from .forms import DataFreshForm
from .models import AFLFixture, AFLTeams, tippings, AFLLadder, tip_ladder
from .forms import TippingForm, CrispyTipping
import requests
import pandas as pd
from sqlalchemy import create_engine
import json
from datetime import date, timedelta, datetime
from django.utils import timezone
from django.forms import formset_factory, modelformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django_tables2 import SingleTableView
from .tables import TippingsTable
import re

User = get_user_model()
users = User.objects.all()

@login_required(login_url='/accounts/google/login/')
def create_tips(request, round_id=None):
    initial = []
    if request.method == 'GET':
        disable_btn = None
        if round_id is None:
                week_start = date.today()
                week_start -= timedelta(days=week_start.weekday())
                week_end = week_start + timedelta(days=7)
                fixture_data = AFLFixture.objects.filter(date__gte=week_start, date__lt=week_end).order_by('date')
                round_id = fixture_data.first().round
        else:
            fixture_data = AFLFixture.objects.filter(round=round_id).order_by('date')

        for item in fixture_data:
            single_tipping = tippings.objects.filter(fixture_id=item.id, email=request.user.email).first()
            if not single_tipping:
                if item.date < timezone.now():
                    status = 'disabled'
                else:
                    status = ''
                initial.append({'fixture_id': item.id, 'hteam': item.hteam, 'ateam': item.ateam, 
                                'hteam_url': item.hteamid.logo, 'ateam_url': item.ateamid.logo, 
                                'date': item.date, 'venue': item.venue, 'status': status, 'margin': 0})
            else:
                item = single_tipping
                if item.date < timezone.now():
                    status = 'disabled'
                else:
                    status = ''
                initial.append({'fixture_id': item.fixture_id, 'hteam': item.hteam, 'ateam': item.ateam, 
                                'hteam_url': item.hteam_url, 'ateam_url': item.ateam_url, 
                                'date': item.date, 'venue': item.venue, 'status': status, 
                                'picks': item.picks, 'margin': item.margin})
        disable_btn = status
        tippingFormSet = formset_factory(CrispyTipping, extra=0)
        formset = tippingFormSet(initial=initial)
        
        context = {'formset': formset,
                'round_id': round_id,
                'pre_url': '/tipping/tips/{}/'.format(int(round_id - 1)), 
                'next_url': '/tipping/tips/{}/'.format(int(round_id + 1)),
                'current_url': '/tipping/tips/{}/'.format(int(round_id)), 
                'disable_btn': disable_btn, 
                'afl_ladder': AFLLadder.objects.all(),
                'tipping_ladder': tip_ladder.objects.all().order_by('rank')}
    if request.method == 'POST':
        resp_data = request.POST.dict()
        fixture_obj = None
        resp_data.pop('csrfmiddlewaretoken')
        print(resp_data)
        if 'margin-score' in resp_data:
            for idx, (key, value) in enumerate(resp_data.items()):
                if idx == 0:
                    fixture_id = re.findall(r'\d+', key)[0]
                    fixture_obj = AFLFixture.objects.filter(id=int(fixture_id))
                    tippings.objects.update_or_create(fixture_id=fixture_id, email=request.user.email, defaults={
                        'first_name': request.user.first_name, 'last_name': request.user.last_name, 
                        'email': request.user.email, 'round': fixture_obj.first().round,
                        'picks': value, 'fixture_id': fixture_id, 'hteam': fixture_obj.first().hteam, 
                        'ateam': fixture_obj.first().ateam, 'date': fixture_obj.first().date,
                        'venue': fixture_obj.first().venue, 'hteam_url': fixture_obj.first().hteamid.logo,
                        'ateam_url': fixture_obj.first().ateamid.logo, 'margin': resp_data['margin-score'],
                        'has_margin': 'yes'
                    })
                elif idx > 1:
                    fixture_id = re.findall(r'\d+', key)[0]
                    fixture_obj = AFLFixture.objects.filter(id=int(fixture_id))
                    tippings.objects.update_or_create(fixture_id=fixture_id, email=request.user.email, defaults={
                        'first_name': request.user.first_name, 'last_name': request.user.last_name, 
                        'email': request.user.email, 'round': fixture_obj.first().round,
                        'picks': value, 'fixture_id': fixture_id, 'hteam': fixture_obj.first().hteam, 
                        'ateam': fixture_obj.first().ateam, 'date': fixture_obj.first().date,
                        'venue': fixture_obj.first().venue, 'hteam_url': fixture_obj.first().hteamid.logo,
                        'ateam_url': fixture_obj.first().ateamid.logo
                    })
            return HttpResponseRedirect('/tipping/tips/{round}/'.format(round=fixture_obj.first().round))
        else:
            for idx, (key, value) in enumerate(resp_data.items()):
                fixture_id = re.findall(r'\d+', key)[0]
                fixture_obj = AFLFixture.objects.filter(id=int(fixture_id))
                tippings.objects.update_or_create(fixture_id=fixture_id, email=request.user.email, defaults={
                    'first_name': request.user.first_name, 'last_name': request.user.last_name, 
                    'email': request.user.email, 'round': fixture_obj.first().round,
                    'picks': value, 'fixture_id': fixture_id, 'hteam': fixture_obj.first().hteam, 
                    'ateam': fixture_obj.first().ateam, 'date': fixture_obj.first().date,
                    'venue': fixture_obj.first().venue, 'hteam_url': fixture_obj.first().hteamid.logo,
                    'ateam_url': fixture_obj.first().ateamid.logo
                })
            return HttpResponseRedirect('/tipping/tips/{round}/'.format(round=fixture_obj.first().round))
    return render(request, 'tipping.html', context)

class TipsView(LoginRequiredMixin, SingleTableView):
    model = tippings
    table_class = TippingsTable
    template_name = 'tips.html'



# Create your views here.
@login_required(login_url='/accounts/google/login/')
def refresh_data(request):
    query_form = DataFreshForm()
    msg = ''
    
    if request.GET.get('refresh_options'):
        query_form = DataFreshForm(request.GET)
        refresh_option = request.GET.get('refresh_options')
        msg = data_refreshing_exec(refresh_option)

    context = {'msg': msg}
    context.update({'form': query_form})

    return render(request, 'data_refresh.html', context)

def data_refreshing_exec(refresh_option):

    if refresh_option == 'Refresh Fixture':
        url = 'https://api.squiggle.com.au/?q=games&year=2023'
        data = requests.get(url).json()['games']
        df = pd.DataFrame.from_records(data)
        for col in df.columns:
            if df[col].dtype == 'float64':
                df[col] = df[col].fillna(-1)
                df[col] = df[col].astype(int)
                df[col] = df[col].astype(str)
                df[col] = df[col].replace('-1', '')
        json_list = json.loads(json.dumps(list(df.T.to_dict().values())))
        for dic in json_list:
            try:
                dic['hteamid'] = AFLTeams(id = int(dic['hteamid']))
            except:
                dic['hteamid'] = None
            try:
                dic['ateamid'] = AFLTeams(id = int(dic['ateamid']))
            except:
                dic['ateamid'] = None
            try:
                dic['winnerteamid'] = AFLTeams(id = int(dic['winnerteamid']))
            except:
                dic['winnerteamid'] = None
            if dic['hbehinds'] == '':
                dic['hbehinds'] = None
            if dic['abehinds'] == '':
                dic['abehinds'] = None
            if dic['hgoals'] == '':
                dic['hgoals'] = None
            if dic['agoals'] == '':
                dic['agoals'] = None
            if dic['hscore'] == '':
                dic['hscore'] = None
            if dic['ascore'] == '':
                dic['ascore'] = None
            AFLFixture.objects.update_or_create(id=dic['id'], defaults=dic)

        return "AFL fixture data has been successfully updated!"
    elif refresh_option == 'Refresh Tippings':
        # Auto-populate tippings data if non-input
        week_start = date.today()
        week_start -= timedelta(days=week_start.weekday())
        week_end = week_start + timedelta(days=7)
        fixture_data = AFLFixture.objects.filter(date__gte=week_start, date__lt=week_end).order_by('date')
        round_id = fixture_data.first().round - 1
        fixture_data = AFLFixture.objects.filter(round=round_id)

        for item in users:
            print(item.first_name, item.last_name, item.email)
            for fixture in fixture_data:
                tippings.objects.get_or_create(email=item.email, fixture_id=fixture.id, defaults={
                        'round': round_id, 'first_name': item.first_name, 'last_name': item.last_name, 'email': item.email,
                        'hteam': fixture.hteam, 'ateam': fixture.ateam, 'date': fixture.date, 'picks': fixture.ateam, 
                        'fixture_id': fixture.id, 'auto': 'yes'})
        # Calculate tipping points
        tps = tippings.objects.all().exclude(status='completed')
        print(tps)
        fixts = AFLFixture.objects.filter(complete=100)
        for item in tps:
            id = item.id
            fixture_id = item.fixture_id
            margin = item.margin
            has_margin = item.has_margin
            fixture = fixts.filter(id=fixture_id).first()
            if fixture is not None:
                try:
                    winner = fixture.winner
                except:
                    winner = None
                if item.picks == winner:
                    tips = 1
                else:
                    tips = 0
                if has_margin == 'yes':
                    margin_diff = abs(margin - abs(int(fixture.hscore) - int(fixture.ascore)))
                else: 
                    margin_diff = 0
                if item.date < timezone.now():
                    status = 'completed'
                else:
                    status = ''
                tippings.objects.filter(id=id).update(tips=tips, margin_diff=margin_diff, status=status, winner=winner)
            else:
                continue
        return "Historical tipping data have been refreshed!"
    elif refresh_option == 'Refresh Tipping Ladder':
        week_start = date.today()
        week_start -= timedelta(days=week_start.weekday())
        week_end = week_start + timedelta(days=7)
        fixture_data = AFLFixture.objects.filter(date__gte=week_start, date__lt=week_end).order_by('date')
        round_id = fixture_data.first().round - 1

        qs = tippings.objects.filter(status='completed').values()
    
        # engine = create_engine('sqlite:///db.sqlite3', echo=True)
        # sqlite_connection = engine.connect()
        # sql = "select * from tipping_tippings where status='completed'"
        # tf = pd.read_sql(sql, engine)
        if len(qs) == 0:
            return "No tipping data available"
        else:
            tf = pd.DataFrame.from_records(qs)
            df1 = tf.groupby(['email', 'first_name', 'last_name'])[['tips', 'margin_diff', 'round']].agg(
                {'tips': 'sum', 'margin_diff': 'sum', 'round': pd.Series.nunique})
            df1 = df1.reset_index()
            df1.columns = ['email', 'first_name', 'last_name', 'total_tips', 'total_margin', 'rounds_tipped']
            df1['avg_per_round'] = df1['total_tips'] / df1['rounds_tipped']
            tf1 = tf.loc[tf['round']==round_id]
            df2 = tf1.groupby('email')[['tips', 'margin_diff']].sum().reset_index()
            df2.columns = ['email', 'last_round_tips', 'last_round_margin']
            df = df1.merge(df2, on='email', how='left')
            df = df.fillna(0)
            df['full_name'] = df['first_name'] + ' ' + df['last_name']
            df = df.sort_values(['total_tips', 'total_margin'], ascending=[False, True])
            df = df.reset_index(drop=True)
            df['rank'] = df.index + 1

            json_list = json.loads(json.dumps(list(df.T.to_dict().values())))
            for dic in json_list:
                tip_ladder.objects.update_or_create(email=dic['email'], defaults=dic)
            return "Tipping ladder refreshed"
    
    elif refresh_option == 'AFL Ladder':
        url = 'https://api.squiggle.com.au/?q=standings;year=2023'
        data = requests.get(url).json()['standings']
        AFLLadder.objects.all().delete()
        for item in data:
            logo = AFLTeams.objects.filter(name=item['name']).first().logo
            AFLLadder.objects.filter(pos=item['rank']).update_or_create(
                pos = item['rank'],
                club = item['name'],
                played = item['played'],
                wins = item['wins'],
                losses = item['losses'],
                draws = item['draws'],
                pts = item['pts'], 
                logo = logo

            )
        return "Ladder data refreshed!"