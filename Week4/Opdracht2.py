import pandas as pd
import numpy as np

df = pd.read_excel("Week4/hotelBookings.xlsx", sheet_name= "hotel_bookings")

# duplicaten weghalen
if df.duplicated().any():
    df = df.drop_duplicates()
else: 
    print("No duplicated")
#print(df['stays_in_week_nights'].astype(int))

data = pd.Series(df['arrival_date_year','arrival_date_month','arrival_date_day_of_month'])

print(data)