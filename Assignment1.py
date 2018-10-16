# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 20:07:05 2018

@author: fatih.dereli
"""

import pandas as pd

PATH = 'C:/Users/fatih.dereli/Desktop/fatih/Personal/mlcourse.ai/Assignment-1/athlete_events.csv'

data = pd.read_csv(PATH)

data.head()

#Q1(14/12)
min(data[(data.Games == "1996 Summer") & (data.Sex == "M")].Age)
min(data[(data.Games == "1996 Summer") & (data.Sex == "F")].Age)

#Q2(1.5)
round(data[(data.Games == "2000 Summer") & (data.Sex == "M") & (data.Sport == "Gymnastics")].Name.nunique()*100.0/data[(data.Games == "2000 Summer") & (data.Sex == "M")].Name.nunique(),1)

#Q3(182.4,9.1)
round(data[(data.Games == "2000 Summer") & (data.Sex == "F")& (data.Sport == 'Basketball')].drop_duplicates().Height.mean(),1)
round(data[(data.Games == "2000 Summer") & (data.Sex == "F")& (data.Sport == 'Basketball')].drop_duplicates().Height.std(),1)

#Q4(Bobsleigh)
data[(data.Games == "2002 Winter") & (data.Weight == max(data[(data.Games == "2002 Winter")].Weight))].Sport

#Q5(3)
data[(data.Name == "Pawe Abratkiewicz")].Games.nunique()

#Q6(2)
data[(data.Games == "2000 Summer") & (data.Team == "Australia") & (data.Sport == "Tennis") & (data.Medal == "Silver")].ID.count()

#Q7(Yes)
swcnt=len(data.dropna(subset=['Medal'])[(data.Games == "2000 Summer") & (data.Team == "Switzerland")])
srcnt=len(data.dropna(subset=['Medal'])[(data.Games == "2000 Summer") & (data.Team == "Serbia")])
swcnt>srcnt

#Q8(45-55,15-25)
bins = [15, 25, 35, 45, 55]
q8=data[(data.Games == "2014 Winter")]
q8['Bins']=pd.cut(q8.Age, bins=bins)
q8.Bins.value_counts()

#Q9(No,Yes)
len(data[(data.Season == "Summer") & (data.City == 'Lake Placid')])>0
len(data[(data.Season == "Winter") & (data.City == 'Sankt Moritz')])>0

#Q10(34)
sp_95=data[(data.Year == 1995)].Sport.nunique()
sp_16=data[(data.Year == 2016)].Sport.nunique()
abs(sp_95-sp_16)
