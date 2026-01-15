import pandas as pd

df = pd.read_csv("Aadhaar_Monthly_Enrolment.csv")

df['date'] = pd.to_datetime(df['date'], dayfirst=True, format='mixed')


df['total'] = df[['age_0_5','age_5_17','age_18_greater']].sum(axis=1)

def detect_anomaly():
    mean = df['total'].mean()
    std = df['total'].std()

    df['Anomaly'] = df['total'] > mean + 2*std
    return df[df['Anomaly']==True][['district','date','total']].to_string()

