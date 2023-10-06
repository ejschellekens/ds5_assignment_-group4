import pandas as pd

df = pd.read_excel("Week4/hotelBookings.xlsx", sheet_name= "hotel_bookings")


#if df.duplicated().any():
  #   df.drop_duplicates()
#else: 
 #   print("No duplicated")

print(df)