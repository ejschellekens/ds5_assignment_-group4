import pandas as pd

def clean_data():
    #Skip first 4 rows
    df = pd.read_excel("Week4/dataProject4.xlsx", sheet_name= "20000-211000", skiprows=4)

    #Rename the columns
    df = df.rename(columns={'HL':'2018(HL)' , 'HL.1':'2019(HL)' , 'HL.2':'2020(HL)' , 'HL.3':'2021(HL)' , 'HL.4':'2022(HL)'})

    #Drop all lines with the results
    dftest = df
    result_rows = dftest['2f. Customer number'].where(dftest['Customer Classification (CRM)'] == ("Result")).dropna()
    df = dftest.drop(result_rows.index)

    #Test for duplicates
    df = df.drop_duplicates()

    return df