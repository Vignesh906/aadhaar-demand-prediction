import pandas as pd

df = pd.read_csv("Aadhaar_Monthly_Enrolment.csv")
df['total'] = df[['age_0_5','age_5_17','age_18_greater']].sum(axis=1)

def mobile_van_plan():
    high = df.groupby('district')['total'].sum().sort_values(ascending=False).head(10)
    return high.to_string()
