#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  7 09:04:54 2022

@author: sandra
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <--- format for read_csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv',sep=';')

#summary of the datat
data.info()

#working with calculations

#Defining variables

CostPerItem=11.73
SellingPricePerItem=21.11
NumberOfItemsPurchased=6


#Mathematical operations on Tableau

ProfitPerItem = 21.11-11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem

CostPerTransaction = CostPerItem * NumberOfItemsPurchased

SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased



#CostPerTransaction column calculation
#CostPerTransaction = CostPerItem * NumberOfItemsPurchased
#Variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#adding a new column to a dataframe

data['CostPerTransaction'] = CostPerTransaction

#sales per transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']


#Profit calculation = sales - cost


data['ProfitPerTransaction'] = data['SalesPerTransaction']-data['CostPerTransaction']

#Markup = (sales - cost)/Cost

data['Markup'] = (data['SalesPerTransaction']-data['CostPerTransaction'])/data['CostPerTransaction']

#rounding markup

roundmarkup = round(data['Markup'],2)

data['Markup'] = round(data['Markup'],2)

#Combining data fields

my_name = 'Sandra'+'Museru'
my_date = 'Day'+'-'+'Month'+'-'+'Year'

#Change column type
day = data['Day'].astype(str)
year = data['Year'].astype(str)

#verify that it worked
print(day.dtype)
print(year.dtype)

my_date = day+'-'+data['Month']+'-'+year
data['date']=my_date

#using iloc to view/locate specific columns/rows
data.iloc[0]  #views the row with the index = 0
data.iloc[0:3]  #views the first 3 rows
data.iloc[-5:]  #views the last 5 rows

data.head(5) #views the first 5 rows

data.iloc[:,2]  #views all the rows for column 2 (columns/rows start from 0)

data.iloc[4,2]  #views the 4th row, 2nd column

#using split to split the client keywords field
#new_var = column.str.split('seperator',expand=True)
#expand=True means that it will continue splitting everything, and will not stop after the frist split

split_col=data['ClientKeywords'].str.split(',',expand=True)


#creating new columns for the split columns in Client Keywords
data['ClientAge'] = split_col[0]  #0 is the name of the column in the split_col table/dataframe
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthofContract'] = data['LengthofContract'].str.replace(']','')

#using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files
#bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv',sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')
data = pd.merge(data,seasons,on='Month')


#dropping columns
#df = df.drop('columnname' , axis=1) 1 is for column, 0 would be for row

data = data.drop('ClientKeywords',axis=1)
data = data.drop('Day',axis=1)
data = data.drop(['Year','Month'],axis=1)

#Export into a csv

data.to_csv('ValueInc_Cleaned.csv',index=False) #we say index=false because we do not want to include the index column































