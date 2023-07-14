import json
from datetime import datetime, timedelta
import pandas as pd

with open('messages.json') as f:
  data = json.load(f)

d = []
m = []
df = pd.DataFrame()

for i in data['messages']:
    d.append(i['timestamp_ms'])

for i in data['messages']:
    x = i.get('content')
    m.append(x)

df['time'] = d
df['message'] = m

df['time'] = pd.to_datetime(df['time'],unit='ms')
time2 = timedelta(days=3)
df['time'] = df['time'] - time2
df.to_csv('messages.csv',index=False)
