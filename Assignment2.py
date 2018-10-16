# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 17:59:30 2018

@author: fatih.dereli
"""
#Importing packages
import numpy as np
import pandas as pd
# pip install seaborn 
import seaborn as sns
import matplotlib.pyplot as plt

#Setting wd
path = 'C:/Users/fatih.dereli/Desktop/fatih/Personal/mlcourse.ai/Assignment-2/2008.csv.bz2'

#Columns to read
dtype = {'DayOfWeek': np.uint8, 'DayofMonth': np.uint8, 'Month': np.uint8 , 'Cancelled': np.uint8, 
         'Year': np.uint16, 'FlightNum': np.uint16 , 'Distance': np.uint16, 
         'UniqueCarrier': str, 'CancellationCode': str, 'Origin': str, 'Dest': str,
         'ArrDelay': np.float16, 'DepDelay': np.float16, 'CarrierDelay': np.float16,
         'WeatherDelay': np.float16, 'NASDelay': np.float16, 'SecurityDelay': np.float16,
         'LateAircraftDelay': np.float16, 'DepTime': np.float16}


#Reading data
flights_df = pd.read_csv(path, usecols=dtype.keys(), dtype=dtype)

#Check the number of rows and columns and print column names.
print(flights_df.shape)
print(flights_df.columns)

#Print first 5 rows of the dataset.
flights_df.head()

#Transpose the frame to see all features at once.
flights_df.head().T

#Examine data types of all features and total dataframe size in memory.
flights_df.info()

#Get basic statistics of each feature.
flights_df.describe().T

#Count unique Carriers and plot their relative share of flights:
flights_df['UniqueCarrier'].nunique()
flights_df.groupby('UniqueCarrier').size().plot(kind='bar');

#finding top-3 flight codes, that have the largest total distance travelled in year 2008.
flights_df.groupby(['UniqueCarrier','FlightNum'])['Distance'].sum().sort_values(ascending=False).iloc[:3]

#Another way:
flights_df.groupby(['UniqueCarrier','FlightNum'])\
  .agg({'Distance': [np.mean, np.sum, 'count'],
        'Cancelled': np.sum})\
  .sort_values(('Distance', 'sum'), ascending=False)\
  .iloc[0:3]
 
#Number of flights by days of week and months:
 pd.crosstab(flights_df.Month, flights_df.DayOfWeek) 
 
#It can also be handy to color such tables in order to easily notice outliers:
 plt.imshow(pd.crosstab(flights_df.Month, flights_df.DayOfWeek),
           cmap='seismic', interpolation='none');
 
#Flight distance histogram:
 flights_df.hist('Distance', bins=20);       

#Making a histogram of flight frequency by date.
flights_df['Date'] = pd.to_datetime(flights_df.rename(columns={'DayofMonth': 'Day'})[['Year', 'Month', 'Day']])
num_flights_by_date = flights_df.groupby('Date').size()
num_flights_by_date.plot();

#Do you see a weekly pattern above? And below?
num_flights_by_date.rolling(window=7).mean().plot();


#Q1(EV)
flights_df[flights_df.Cancelled==0].groupby(['UniqueCarrier']).size().sort_values(ascending=False).iloc[:10]

#Q2(Weather)
flights_df[flights_df.Cancelled==1].groupby(['CancellationCode']).size().plot(kind='bar')

#A	Carrier
#B	Weather
#C	National Air System
#D	Security

#Q3(San-Francisco – Los-Angeles)
flights_df.groupby(['Origin','Dest']).size().sort_values(ascending=False).iloc[:5]

#Q4(668)
delayed = flights_df[(flights_df.CarrierDelay > 0.0) | (flights_df.WeatherDelay > 0.0) |(flights_df.NASDelay > 0.0) |(flights_df.SecurityDelay > 0.0) |(flights_df.LateAircraftDelay > 0.0) ]
delayed = flights_df[(flights_df.DepDelay > 0.0)]
top5delay=delayed.groupby(['Origin','Dest']).size().sort_values(ascending=False).iloc[:5]
d1=delayed[(delayed.Origin == 'LAX') & (delayed.Dest == 'SFO') & (delayed.WeatherDelay > 0.0)].Year.count()
d2=delayed[(delayed.Origin == 'DAL') & (delayed.Dest == 'HOU') & (delayed.WeatherDelay > 0.0)].Year.count()
d3=delayed[(delayed.Origin == 'SFO') & (delayed.Dest == 'LAX') & (delayed.WeatherDelay > 0.0)].Year.count()
d4=delayed[(delayed.Origin == 'ORD') & (delayed.Dest == 'LGA') & (delayed.WeatherDelay > 0.0)].Year.count()
d5=delayed[(delayed.Origin == 'HOU') & (delayed.Dest == 'DAL') & (delayed.WeatherDelay > 0.0)].Year.count()
d1+d2+d3+d4+d5

#Q5(Only 3rd option)
flights_df[(flights_df.DepTime >0)].groupby([DepTime.str[0:2]]).size().plot(kind='bar')
deps=flights_df[(flights_df.DepTime >0)].DepTime
deps=round(flights_df.loc[flights_df.DepTime.notna()].DepTime/100)
deps.plot(kind='density')

#Q6(Option 1 and 3)
flights_df.groupby(['DayOfWeek']).size().sort_values(ascending=False)
flights_df.groupby(['Month']).size().sort_values(ascending=False)

#Q7(Option 1 and 3)
flights_df[(flights_df.Cancelled==1) & (flights_df.Month == 12)].groupby(['CancellationCode']).size().plot(kind='bar')
flights_df[(flights_df.Cancelled==1) & (flights_df.Month == 9)].groupby(['CancellationCode']).size().plot(kind='bar')
flights_df[(flights_df.Cancelled==1) & (flights_df.Month == 4)].groupby(['CancellationCode']).size().plot(kind='bar')
flights_df[flights_df.Cancelled==1].groupby(['CancellationCode']).size().plot(kind='bar')

#^Q8(April)
flights_df[(flights_df.Cancelled==1) & (flights_df.CancellationCode == 'A')].groupby(['Month']).size().plot(kind='bar')

#Q9(AA)
flights_df[(flights_df.Cancelled==1) & (flights_df.CancellationCode == 'A')& (flights_df.Month == 4)].groupby(['UniqueCarrier']).size().plot(kind='bar')

#Q10(OO)?
flights_df.groupby('UniqueCarrier')[['ArrDelay','DepDelay']].median()
