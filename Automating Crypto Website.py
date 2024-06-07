#!/usr/bin/env python
# coding: utf-8

# In[7]:


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'20',  #reduced my limit to 20 so it's easier to handle at a time
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '2528c72e-da65-4924-8682-3e95e86de3a6',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


# In[ ]:





# In[24]:


import pandas as pd

pd.set_option('display.max_columns', None) #THIS ensures all the rows are visible
pd.set_option('display.max_rows', None)


# In[9]:


df = pd.json_normalize(data['data']) # this organizes all the rows and columns

df['timestamp'] =  pd.to_datetime('now') #this shows time stamp for when we execute the code

df


# In[ ]:





# In[30]:


def api_runner():
    
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'20',  #reduced my limit to 20 so it's easier to handle at a time
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '2528c72e-da65-4924-8682-3e95e86de3a6',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    
    df= pd.json_normalize(data['data']) # this organizes all the rows and columns
    df['timestamp'] =  pd.to_datetime('now') #this shows time stamp for when we execute the code
    df
    
 # df2 = pd.json_normalize(data['data']) # this organizes all the rows and columns
#df2['timestamp'] =  pd.to_datetime('now') #this shows time stamp for when we execute the code
#df = df.append(df2) # made it df2 so it does not affect previous df1 before appending it. This also loops df through df2.
        
    
    #converting this to a CSV file
    
    if not os.path.isfile(r'/Users/Joshua/Documents/DS Begins\CryptoAPI.csv'): #if this file exists
        df.to_csv(r'/Users/Joshua/Documents/DS Begins\CryptoAPI.csv', header='column_names') #save like this
    else:
        df.to_csv(r'/Users/Joshua/Documents/DS Begins\CryptoAPI.csv', mode = 'a', header = False) #else, don't


# In[10]:


# automating my python script


# In[31]:


import os
from time import time
from time import sleep #this gives us the ability to track time. to also call the api_runner function in intervals we want.

for i in range(333):
    api_runner()
    print('API Runner completed')
    sleep(60)
exit()


# In[38]:


df5 = pd.read_csv(r'/Users/Joshua/Documents/DS Begins\CryptoAPI.csv')
df5


# In[39]:


df


# In[40]:


#pd.set_options('display.float_format', lambda x: '%.5f' %x)

import pandas as pd

pd.options.display.float_format = '{:.5f}'.format #changed the format of the numebers from 603+1e to proper float


# In[41]:


df


# In[46]:


df6 = df.groupby('name', sort=False)[['quote.USD.percent_change_1h', 'quote.USD.percent_change_24h', 'quote.USD.percent_change_7d', 'quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d']].mean()
df6 #we wanted to find the average for the percentage change for different time frame


# In[47]:


df7 = df6.stack()
df7 #given that we want to visualize it, we have to stack it. 


# In[49]:


type(df7) #after stacking, we realized the data type was no longer a dataframe but a series. 


# In[52]:


df8 = df7.to_frame(name='values')  #so we changed it to a dataframe here. 
df8  


# In[53]:


type(df8)


# In[55]:


df8.count()


# In[ ]:


#the 'name' above is an index; it's not ideal because it won't be added to our visualization if we leave it that way
#so we have to give it a new index. the normal way of 'df8.set_index(df8['name'])' wont work here. so we have to do something else


# In[ ]:





# In[58]:


index = pd.Index(range(120)) #created the index

df9 = df8.reset_index() #reset the index to correct the values itself
df9


# In[59]:


df10 = df9.rename(columns={'level_1': 'percentage_change'}) #changed the header name
df10


# In[ ]:


#visualizations - importing seaborn and matlplotlib


# In[63]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:





# In[62]:


sns.catplot(x='percentage_change', y='values', hue='name', data = df10, kind = 'point') #setting my parameters


# In[ ]:


#I noticed the x axis is a bit messy because of the names. I will have to change that. 


# In[70]:


df10['percentage_change'] = df10['percentage_change'].replace(['quote.USD.percent_change_1h','quote.USD.percent_change_24h',
                                 'quote.USD.percent_change_7d','quote.USD.percent_change_30d',
                                 'quote.USD.percent_change_60d','quote.USD.percent_change_90d',], 
                                  ['1h', '24h', '7d', '30d', '60d', '90d'])
#replaced the headers with the appropriate parameters
df10


# In[71]:


sns.catplot(x='percentage_change', y='values', hue='name', data = df10, kind = 'point')


# In[72]:


#simpler visualization


# In[74]:


df11 = df[['name', 'quote.USD.price', 'timestamp']]
df11


# In[78]:


df11 = df[['name', 'quote.USD.price', 'timestamp']]
df11 = df11.query("name == 'Ethereum'")
df11


# In[79]:


sns.set_theme(style = "darkgrid")

sns.lineplot(x='timestamp', y = 'quote.USD.price', data = df11)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




