#!/usr/bin/env python
# coding: utf-8

# # IMPORTING LIBRARIES

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings ("ignore")


# # Loading the Dataset 

# In[2]:


df = pd.read_csv('hotel_bookings 2.csv')


# # Exploratory Data Analysis and Cleaning 

# In[3]:


#df.head(), will give 5 top rows of the table, as long no value is provided to head 

df.head()


# In[4]:


#df.tail(), will give 5 bottom rows of the table 

df.tail()


# In[5]:


#gf.shape tells the total number of rows and column in the existing table 

df.shape


# In[6]:


df.columns


# In[7]:


#df.info(), will give the data types of the table

df.info()


# In[8]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'], format='%d/%m/%Y')  #here we are changing the
#format of the date and time and need to make sure that we give the wanted FORMAT in the end

print(df['reservation_status_date'])


# In[9]:


df.info()


# In[10]:


df.describe(include = 'object')


# In[11]:


for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())
    print("-" * 50)


# In[12]:


df.isnull().sum()


# In[13]:


#removing missing value 

df.drop(['company', 'agent'], axis = 1, inplace = True)
df.dropna(inplace=True)


# In[14]:


df.isnull().sum()


# In[15]:


df.describe()


# In[16]:


#filtering the valkue for adr which is more than 5000

df = df[df['adr']<5000] 


# In[17]:


df.describe()


# # Data Analysis and Visualisation

# In[18]:


cancelled_perc = df['is_canceled'].value_counts(normalize=True)
print(cancelled_perc)


# In[19]:


plt.figure(figsize=(5, 4))
plt.title('Reservation Status')
plt.bar(['Not canceled', 'Canceled'], df['is_canceled'].value_counts(), edgecolor='k', width=0.5)
plt.show()


# In[20]:


import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(5, 4))
ax1 = sns.countplot(x='hotel', hue='is_canceled', data=df, palette='Blues')
legend_labels, _ = ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1, 1))
plt.title('Reservation status in different hotels', size=20)
plt.xlabel('Hotel')
plt.ylabel('Number of reservations')
plt.show()



# In[21]:


#checking percentage of cancelation in resort hotel
resort_hotel = df[df['hotel'] == 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize = True)



# In[22]:


city_hotel = df[df['hotel'] == 'City Hotel']
city_hotel['is_canceled'].value_counts(normalize = True)


# In[23]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel = city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[24]:


plt.figure(figsize=(30,10))
plt.title('Average daily rates in Resort and City hotel', fontsize = 20)
plt.plot(resort_hotel.index, resort_hotel['adr'], label = 'Resort Hotel')
plt.plot(city_hotel.index, city_hotel['adr'], label = 'City Hotel')
plt.legend(fontsize = 25)
plt.show()


# In[25]:


#here we will find out monthly cancelation and not-canceled ratio

df['month']=df['reservation_status_date'].dt.month
plt.figure(figsize = (16,8))
ax1 = sns.countplot(x= 'month', hue = 'is_canceled', data = df, palette = 'bright')
legend_labels,_ = ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor= (1,1))
plt.title('Reservation status per month', size = 20)
plt.xlabel('month')
plt.ylabel('number of reservations')
plt.legend(['not canceled', 'canceled'])
plt.show()


# In[26]:


#here we are checking average daily rate per month 

plt.figure(figsize = (15,8))
plt.title('ADR per month', fontsize = 30)
sns.barplot(x = 'month',y = 'adr', data = df[df['is_canceled']==1].groupby('month')['adr'].sum().reset_index())
plt.show()


# In[27]:


#finding out which country has the highest cancelation

canceled_data = df[df['is_canceled'] == 1]
top_10_countries = canceled_data['country'].value_counts()[:10]  #this will give data for the top 10 countries 

plt.figure(figsize = (8,8))
plt.title('Top 10 coutries with highest cancelation')
plt.pie(top_10_countries, autopct = '%.2f', labels = top_10_countries.index)
plt.show()


# In[28]:


#checking output, which source has the most reservation at the hotel 

df['market_segment'].value_counts()


# In[29]:


#checking which source has the most cancelation 

canceled_data['market_segment'].value_counts(normalize = True )


# In[30]:


canceled_df_adr = canceled_data.groupby('reservation_status_date')['adr'].mean().reset_index()
canceled_df_adr.sort_values('reservation_status_date', inplace=True)

not_canceled_data = df[df['is_canceled'] == 0]
not_canceled_df_adr = not_canceled_data.groupby('reservation_status_date')['adr'].mean().reset_index()
not_canceled_df_adr.sort_values('reservation_status_date', inplace=True)

plt.figure(figsize=(20, 6))
plt.title('Average Daily Rate', fontsize = 15)
plt.plot(not_canceled_df_adr['reservation_status_date'], not_canceled_df_adr['adr'], label='Not Canceled')
plt.plot(canceled_df_adr['reservation_status_date'], canceled_df_adr['adr'], label='Canceled')
plt.xlabel('Reservation Status Date')
plt.ylabel('Average Daily Rate')
plt.legend()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




