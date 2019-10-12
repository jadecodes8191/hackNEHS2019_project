# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

from fbprophet import Prophet
import pandas as pd

def predict(filename, futures=365):
    df = pd.read_csv(filename)
    df['cap'] = 1
    m = Prophet()
    m.fit(df)
    future = m.make_future_dataframe(periods=futures)
    future['cap'] = 1
    forecast = m.predict(future)
    return (forecast, m.plot(forecast))