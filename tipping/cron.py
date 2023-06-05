import requests
import pandas as pd
from sqlalchemy import create_engine


def update_afl_fixture():
    engine = create_engine('sqlite:///db.sqlite3', echo=True)
    sqlite_connection = engine.connect()
    url = 'https://api.squiggle.com.au/?q=games&year=2023'
    data = requests.get(url).json()['games']
    df = pd.DataFrame.from_records(data)
    df.to_sql('tipping_fixture', sqlite_connection, if_exists='fail')

    return True

def update_tippings():
    pass

def update_ladder():
    pass