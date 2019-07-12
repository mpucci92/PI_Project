#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as pdr
from pandas_datareader import data
import fix_yahoo_finance as yf
yf.pdr_override() 

#Importing the date
import datetime
now = datetime.datetime.now()
currenttime = now.strftime("%Y-%m-%d")
print(currenttime)


# In[46]:


symbol = 'FB'
data_source='google'
start_date = '2013-01-01'
end_date = currenttime
df = data.get_data_yahoo(symbol, start_date, end_date)


# In[47]:


print (df.columns)

#STEP 3:
#Check each column in data to see if there exists NaN or Null Values 
null_columns = []
nullvalue_columns = []


for column in df:
    if df[column].isnull().any():
        print('{0} has {1} null values'.format(column, df[column].isnull().sum()))
        nullvalue_columns.append(df[column].isnull().sum())
        null_columns.append(column)
    
null_table = pd.DataFrame(columns=['Feature','Nullvalue'])
null_table['Feature'] = null_columns
null_table['Nullvalue'] = nullvalue_columns 
print(null_table)


# In[48]:


num_cols = df._get_numeric_data().columns

for column in df.columns:
    
    if column in (num_cols):
        median_values = df[column].median()
        df[column] = df[column].dropna()
        df[column].fillna(median_values)
    else:
        mode_values = df[column].mode()[0]
        df[column] = df[column].dropna()
        df[column] = df[column].fillna(mode_values)


# In[49]:


#Confimration that Null Values have been removed
for column in df:
    if df[column].isnull().any():
        print('{0} has {1} null values'.format(column, df[column].isnull().sum()))    

for column in df:
    value_count = df[column].value_counts(dropna=False)
    #print(value_count) print all unique values for each row


# In[51]:


#STEP 5: Lets Visualize the data in our columns for outliers 
features = df.iloc[:,1:]
print (features.head())

for column in features:
    a = df[column].values
    plt.hist(a,bins=20,color=['Orange'])   #Number of bins can be configured to show smaller gorups in histogram 
    plt.title(column)
    plt.show()


# In[35]:


#STEP 6: Drop Duplicate timestamp rows 
timestamp = df.iloc[:,0]
timestamp = timestamp.drop_duplicates()

clean_data = pd.DataFrame()
clean_data['Open'] = df['Open']
clean_data['Close'] = df['Close']
clean_data['High'] = df['High']
clean_data['Low'] = df['Low']
clean_data['Volume'] = df['Volume']

print(clean_data.head()) 


# In[36]:


#Name of Script 
clean_data.to_csv(r'\\rsingh1-client\\C$\\Output\\FB_clean.csv') 


# In[ ]:





# In[ ]:




