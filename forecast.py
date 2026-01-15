

import pandas as pd
from prophet import Prophet

df = pd.read_csv("Aadhaar_Monthly_Enrolment.csv")
df['date'] = pd.to_datetime(df['date'], dayfirst=True, format='mixed')

def forecast_demand(district):
    d = df[df['district'].str.upper() == district.upper()]
    d['total'] = d[['age_0_5','age_5_17','age_18_greater']].sum(axis=1)

    data = d[['date','total']]
    data.columns = ['ds','y']

    model = Prophet()
    model.fit(data)

    future = model.make_future_dataframe(periods=6, freq='M')
    forecast = model.predict(future)

    return forecast[['ds','yhat']].tail(6).to_string()
