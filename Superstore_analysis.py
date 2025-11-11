#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 16:12:18 2025

@author: siddu
"""

import pandas as pd 

data=pd.read_csv('/Users/siddu/Downloads/Sample - Superstore.csv')

data=pd.read_csv('/Users/siddu/Downloads/Sample - Superstore.csv',encoding='latin1')


data.head()

data.info()

data['Order Date']=pd.to_datetime(data['Order Date'])

data['Order Date'].dt.year

data['Ship Date']=pd.to_datetime(data['Ship Date'])

data['Ship Date'].dt.month

data.info()

data.isna().sum()

data.duplicated().sum()

data=data.drop_duplicates()

data.shape

data['Order_year']=data['Order Date'].dt.year

data['Order_month']=data['Order Date'].dt.month

data['Order_day_ofweek']=data['Order Date'].dt.day_name()

data['Order_day_ofweek'].head()

data.columns

data['Delivery_Days']=data['Ship Date'] - data['Order Date'] # here after this calculation we get timedelta dtype 

data['Delivery_Days'].head(10)

data.info()

data['Delivery_Days']=(data['Ship Date']-data['Order Date']).dt.days

data['Delivery_Days'].head()

data.info()

data.describe()

data['Delivery_Days'].describe()

data['Profit_margin']=data['Profit']/data['Sales']

data['Profit_margin'].head(10)

data['Sales_per_unit']=data['Sales']/data['Quantity']

data['Sales_per_unit'].head(10)

data['Sales_per_unit'].max()

data.loc[data['Sales_per_unit']==3773.08,'Product Name']

data[data['Sales_per_unit']==3773.08]

data.columns


data[['Order Date','Ship Date','Delivery_Days','Profit_margin','Sales_per_unit','Order_year','Order_month','Order_day_ofweek']].head()

data.describe()

data.groupby('Region').agg({'Sales':'sum','Profit':'sum'}).sort_values('Sales',ascending=False)

data.groupby('Category')['Sales'].sum().sort_values(ascending=False)

data.groupby('Category').agg({'Sales':'sum'}).sort_values('Sales',ascending=False)

data.columns



data.groupby('Sub-Category')['Profit_margin'].mean().sort_values(ascending=False)

data.groupby('Sub-Category').agg({'Profit_margin':'mean'}).sort_values('Profit_margin',ascending=False)

data.groupby('Order_month')['Sales'].sum().sort_values(ascending=False)

monthly_sales=data.groupby('Order_month')['Sales'].sum().reset_index()

monthly_sales=data.groupby('Order_month',as_index=False)['Sales'].sum()




monthly_sales.head()

import matplotlib.pyplot as plt 

import seaborn as sns

sns.lineplot(x='Order_month',y='Sales',data=monthly_sales)

plt.show()

sns.lineplot(x='Order_month',y='Sales',data=monthly_sales,marker='o')
plt.title('Monthly Sales Trend ')
plt.xlabel('Month')
plt.ylabel('Total sales by month')
plt.show()

## total sales and profit by category 

category_pref=data.groupby('Category',as_index=False).agg(total_sales=('Sales','sum'),total_profit=('Profit','sum')).sort_values('Category')


category_pref.head()

## barplot for total sales by category
sns.barplot(x='Category',y='total_sales',data=category_pref)
plt.title('Total Sales by category')
plt.show()


## barplot for total profit by category 

sns.barplot(x='Category',y='total_profit',data=category_pref)
plt.title('total profit by category')
plt.show()

## total sales and profit by region 

region_perf=data.groupby('Region')[['Sales','Profit']].sum().reset_index()

region_perf.head()

## barplot for total sales by region 

sns.barplot(x='Region',y='Sales',data=region_perf)
plt.ylabel('Total sales')
plt.title('total sales by region')
plt.show()

#line plot for total profit by region 

sns.lineplot(x='Region',y='Profit',data=region_perf,marker='o')
plt.title('Line plot for total profit by region ')
plt.ylabel('total profit')
plt.show()

## avg profit margin by region 
data['Profit_margin'].head()


profit_mar=data.groupby('Region',as_index=False)['Profit_margin'].mean()

profit_mar.head()


# barplot 
sns.barplot(x='Region',y='Profit_margin',data=profit_mar)
plt.ylabel('AVG profit margin')
plt.title('avg profit margin by region ')
plt.show()




sns.lineplot(x='Region',y='Profit_margin',data=profit_mar)
plt.ylabel('AVG profit margin')
plt.title('avg profit margin by region ')
plt.show()


## top 10 products by sales 

top_10products=data.groupby('Product Name',as_index=False)['Sales'].sum().sort_values('Sales',ascending=False).head(10)

top_10products.head()

## plotting top 10 products by sales 
import matplotlib.pyplot as plt 
import seaborn as sns

sns.barplot(y='Product Name',x='Sales',data=top_10products)
plt.title('Top 10 products by sales')
plt.ylabel('Top 10 products')
plt.show()

# scatter is used to find relationship between two variables 
sns.scatterplot(y='Profit',x='Discount',data=data)
plt.title('Realtionship between profit and discount')
plt.show()

data[['Sales', 'Profit', 'Discount', 'Quantity']].corr()

data.to_csv('/Users/siddu/Downloads/Superstore_Cleaned.csv', index=False)


## region summary

region_summary=data.groupby('Region',as_index=False).agg({'Sales':'sum','Profit':'sum','Quantity':'sum'})

region_summary

region_summary.columns

region_summary['profit_margin']=region_summary['Profit']/region_summary['Sales']


region_summary.to_csv('/Users/siddu/Downloads/Region_Summary.csv', index=False)


## category summary

category_summary=data.groupby('Category',as_index=False).agg({'Sales':'sum','Profit':'sum','Quantity':'sum'})

category_summary


category_summary['profit_margin']=category_summary['Profit']/category_summary['Sales']


category_summary.to_csv('/Users/siddu/Downloads/Category_Summary.csv', index=False)


## monthly summary 

data['YearMonth'] = data['Order Date'].dt.to_period('M')


data['YearMonth'].dtype

data['YearMonth'].head()

data['YearMonth'].sort_values()

data['YearMonth']=data['Order Date'].dt.to_period('M').astype(str)

data['YearMonth'].dtype

monthly_summary = data.groupby('YearMonth', as_index=False).agg({
    'Sales':'sum', 'Profit':'sum'
})
monthly_summary['Profit_Margin'] = monthly_summary['Profit'] / monthly_summary['Sales']
monthly_summary.to_csv('/Users/siddu/Downloads/Monthly_Summary.csv', index=False)


## segment summary 

segment_summary = data.groupby('Segment', as_index=False).agg({
    'Sales':'sum', 'Profit':'sum', 'Quantity':'sum'
})
segment_summary['Profit_Margin'] = segment_summary['Profit'] / segment_summary['Sales']
segment_summary.to_csv('/Users/siddu/Downloads/Segment_Summary.csv', index=False)



data.to_csv('/Users/siddu/Downloads/Superstore_Cleaned.csv', index=False)




