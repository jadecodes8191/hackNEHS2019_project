#Test

import pandas as pd
import csv

jan = pd.read_csv("jan.csv")
feb = pd.read_csv("feb.csv")
mar = pd.read_csv("mar.csv")
apr = pd.read_csv("apr.csv")
may = pd.read_csv("may.csv")
jun = pd.read_csv("jun.csv")
jul = pd.read_csv("jul.csv")
aug = pd.read_csv("aug.csv")

total = pd.merge(jan, feb)
for df in [mar, apr, may, jun, jul, aug]:
    total = pd.merge(total, df, how='outer')


total['On-Time Percent'] = (total['otp_numerator']/total['otp_denominator'])*100

total = total.sort_values('On-Time Percent')

total_copy = total.dropna(subset=['On-Time Percent'])
print(total_copy)

# print(total)
