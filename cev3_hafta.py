# -*- coding: utf-8 -*-
"""Cev3.Hafta.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MgQjhMD20rePkHGPodEhyorKwkUg8yHj
"""

import pandas as pd #nüfus ve alan serileri üzerinden df oluşturma
cities_population=pd.Series([4425789,3147818,15840900,5747325,602567], index=["İzmir", "Bursa","İstanbul", "Ankara", "Tokat"])
print(cities_population)
area=pd.Series([11891,10813,5461,25632,10042], index=["İzmir", "Bursa", "İstanbul","Ankara","Tokat"])
print(area)
info_of_cities=pd.DataFrame({"Population": cities_population, "Area": area})
info_of_cities

inda=pd.Index([1,2,3,4]) #index fonksiyon örnekleri
indb=pd.Index([1,2,3,7,6])
a=inda & indb #kesişim
b=inda ^ indb #farklarını
c=inda| indb #birleştirme
print(a)
print(b)
print(c)

maskOfPopulation= (cities_population<1000000) #maskeleme ile görüntüleme 
print(cities_population[maskOfPopulation])
maskOfArea=(area>5000)
print(area[maskOfArea])

info_of_cities["density"]=info_of_cities["Population"]/info_of_cities["Area"]
a=info_of_cities.T #yoğunluk adında kolon ekleme
a

df=info_of_cities.loc[(info_of_cities.density > 100), ["Population","density"]] #nüfus ve yoğunluğu gösterme
df

import numpy as np #dataframe'deki boşlukları doldurma 
rng=np.random.RandomState(42)
a=pd.DataFrame(rng.randint(0,49,(6,8)))
print(a)
a.iloc[3,3]=np.nan
a.iloc[0,2]=np.nan
print(a)
a.fillna(method="ffill",axis=1)

cc=[("izmir",2020), ("izmir",2019), ("ankara",2020),("ankara",2019),("istanbul",2020),("istanbul",2019)]
cities_population=pd.Series([4394694,4367259,5663322,5639076,15462452,15519267], index=(cc)) #multi indexleme yöntemi ile dataframe oluşturma    
#burada mulkti indexi sadece population serisi üzerinden yaptık sornasında df oluşturulurken pandasın verdiği bir özellik olarak oto diğerine de uyguladı
index=pd.MultiIndex.from_tuples(cc)
pop=cities_population.reindex(index)
area=pd.Series([11891,11891,5461,5461,25632,25632], index=(cc))
df=pd.DataFrame({"population":pop,"Area":area})
df1=df["density"]=df["population"]/df["Area"]
df.unstack()

import pandas as pd #merge task
df1 = pd.DataFrame({"city": ["izmir", "ankara", "istanbul"],
                    "population": [4394694,5663322,15462452]})
df2 = pd.DataFrame({"city": ["izmir", "ankara", "istanbul"],
                    'area': [11891,5461,25632]})
pd.merge(df1,df2)