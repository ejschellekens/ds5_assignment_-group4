import pandas as pd
import numpy as np

df = pd.read_excel("Week4/hotelBookings.xlsx", sheet_name= "hotel_bookings")

# duplicaten weghalen
if df.duplicated().any():
    df = df.drop_duplicates()

# Aantal nacht in een kolom 
df['stay_in_nights'] = df['stays_in_weekend_nights']+df['stays_in_week_nights'].astype(int)

# Aantal gasten
df['total_guest'] = df['adults']+df['children']+df['babies'].astype(int)

# arrival in datetime zetten
df['datum'] = df['arrival_date_year'].astype(str) + ' ' + df['arrival_date_month'] + ' ' + df['arrival_date_day_of_month'].astype(str)
df['date_in_datatime'] = pd.to_datetime(df['datum'], format='%Y %B %d')
df['arrival_date'] = df['date_in_datatime'].dt.strftime('%d-%m-%Y')

for index, row in df.iterrows():
    reservation = row['reservation_status']
    arrival = row['arrival_date']
    country = row['country']
    # Mensen die niet niet komen hebben geen data in arrival_date
    if reservation == 'Canceled' or reservation == 'No-Show':
        df.at[index, 'arrival_date'] = None
    # Rijen met verkeerde gegevens weghalen    
    if country == 2 or country ==3:
        df.at[index, 'country'] = None

# kolommen weghalen die overbodig zijn
# Kolommen 'is_repeated_guest','previous_cancellations','previous_bookings_not_canceled',  
# 'days_in_waiting_list' en 'deposit_type' hebben alleen nullen of No Deposit, het is niet nodig om die data te analyseren.
df.drop(['is_canceled','arrival_date_year','arrival_date_month',
         'arrival_date_week_number','arrival_date_day_of_month',
         'stays_in_weekend_nights', 'stays_in_week_nights','adults',
         'children','babies','is_repeated_guest','previous_cancellations',
         'previous_bookings_not_canceled','deposit_type','days_in_waiting_list','datum',
        'date_in_datatime'], axis=1, inplace=True)

# Index op goede volgorde zetten
df = df.reset_index(drop=True)

print(df)