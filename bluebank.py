#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 14:45:14 2022

@author: sandra
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data
json_file=open('loan_data_json.json')
data=json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file:
    data=json.load(json_file)

#transform to dataframe
loandata = pd.DataFrame(data)

#finding unique values for the purpose column
loandata['purpose'].unique()

#describe the data
loandata.describe()

#describe the data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using EXP() to get the annual income
income=np.exp(loandata['log.annual.inc'])
loandata['annualincome']=income

#working with arrays
#1D array
arr=np.array([1,2,3,4])

#0D array
arr=np.array(43)

#2D array
arr=np.array([[1,2,3],[4,5,6]])


#working with IF statements
a=40
b=500

if b>a:
    print('b is greater than a')

#let's add more conditions
a=40
b=500
c=1000

if b>a and b<c:
    print('b is greater than a but less than c')

#What if a condition is not met
a=40
b=500
c=20

if b>a and b<c:
    print('b is greater than a but less than c')
else:
    print('No condition met')

#another condition different metrics
a=40
b=0
c=30

if b>a and b<c:
    print('b is greater than a but less than c')
elif b>a and b>c:
    print('b is greater than a and c')
else:
    print('No conditions met')

#Using OR
a=40
b=500
c=30

if b>a or b<c:
    print('b is greater than a or less than c')
else:
    print('No conditions met')    


#FICO Score
fico=250

# fico >= 300 and < 400: 'Very Poor'
# fico >= 400 and ficoscore < 600: 'Poor'
# fico >= 601 and ficoscore < 660: 'Fair'
# fico >= 660 and ficoscore < 780: 'Good'
# fico >=780: 'Excellent'

if fico>=300 and fico<400:
    ficocat='Very Poor'
elif fico>=400 and fico<600:
    ficocat='Poor'
elif fico>=600 and fico<660:
    ficocat='Fair'
elif fico>=660 and fico<780:
    ficocat='Good'
elif fico>=780:
    ficocat='Excellent'
else:
    ficocat='Unkown'
print(ficocat)

#for loops
fruits=['apple', 'pear','banana','cherry']
for x in fruits:
    print(x)
    y=x+' fruit'
    print(y)
    
for x in range(0,4):
    y=fruits[x]
    print(y)
    
#applying forloops to loan data
#using first 10
length=len(loandata)
ficocat=[]
for x in range(0,length):
    category=loandata['fico'][x]
    
    try: #the try statement allows me to run the code even if there is an error
        if category>=300 and category<400:
            cat='Very Poor'
        elif category>=400 and category<600:
            cat='Poor'
        elif category>=600 and category<660:
            cat='Fair'
        elif category>=660 and category<780:
            cat='Good'
        elif category>=780:
            cat='Excellent'
        else:
            cat='Unknown'
    except:
        cat='Unknown'
        
    ficocat.append(cat)
ficocat=pd.Series(ficocat)

loandata['fico.category']=ficocat


#while loops
i=1
while i<10:
    print(i)
    i=i+1

#df.loc as conditional statements
# df.loc[df[columnname]condition, new columnname]='value if the condition is met'

loandata.loc[loandata['int.rate']>0.12, 'int.rate.type']='High'
loandata.loc[loandata['int.rate']<=0.12, 'int.rate.type']='Low'

#number of loans/rows by fico.cat

catplot=loandata.groupby(['fico.category']).size()
catplot.plot.bar(color='green',width=0.2)
plt.show()


purplot=loandata.groupby(['purpose']).size()
purplot.plot.bar(color='orange',width=0.2)
plt.show()
    
#scatterplot

xpoint=loandata['dti']
ypoint=loandata['annualincome']
plt.scatter(xpoint,ypoint)
plt.show()


#Writing to csv
loandata.to_csv('loan_cleaned.csv',index=True)










































































