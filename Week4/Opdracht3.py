import pandas as pd

df = pd.read_excel("Week4/detailedRetail.xlsx")

#Total sales per category
sales_per_category = df.groupby('Category')['Sales'].sum().reset_index()

#Percentage that a category contributes to the total sales
total_sales = df['Sales'].sum()
sales_per_category['Percentage'] = (sales_per_category['Sales'] / total_sales) * 100

#Sales for each month
sales_per_month = df.groupby('Month')['Sales'].sum().reset_index()

#Percentage that the month contributes to the total
sales_per_month['Percentage'] = (sales_per_month['Sales'] / total_sales) * 100

#Sales for each sales manager
sales_per_manager = df.groupby('Sales Manager')['Sales'].sum().reset_index()

#Percentage that the sales manager contributes to the total
sales_per_manager['Percentage'] = (sales_per_manager['Sales'] / total_sales) * 100

#Create report
report = pd.concat([sales_per_category, sales_per_month, sales_per_manager], ignore_index=True)

#Export report to excel
report.to_excel("Week4/reportRetail.xlsx")
