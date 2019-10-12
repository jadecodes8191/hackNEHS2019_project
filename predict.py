# -*- coding: utf-8 -*-

from fbprophet import Prophet
import pandas as pd

def predict(filename, futures=365):
    df = pd.read_csv(filename)
    df['cap'] = 1
    m = Prophet()
    m.fit(df)
    future = m.make_future_dataframe(periods=futures)
    future['cap'] = 1
    future = future[future['ds'].dt.weekday < 5]
    forecast = m.predict(future)
    return (df, forecast)