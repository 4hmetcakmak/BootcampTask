# -*- coding: utf-8 -*-
"""12.04calsswork.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ThpwDWDrWLqmaF22AfLAM87Ue-FoGw3J
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from sklearn.datasets import fetch_20newsgroups 

data = fetch_20newsgroups() 
data.target_names

categories=["rec.autos", "sci.med","misc.forsale","rec.motorcycles","sci.crypt"]
train = fetch_20newsgroups(subset='train', categories=categories) 
test = fetch_20newsgroups(subset='test', categories=categories)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB 
from sklearn.pipeline import make_pipeline 

model = make_pipeline(CountVectorizer(), MultinomialNB())

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB 
from sklearn.pipeline import make_pipeline 

model1 = make_pipeline(TfidfVectorizer(), MultinomialNB())

model.fit(train.data, train.target) #count
labels = model.predict(test.data)

model1.fit(train.data, train.target) #tfid
labels1 = model1.predict(test.data)

from sklearn.metrics import confusion_matrix #Count
mat = confusion_matrix(test.target, labels)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=train.target_names, yticklabels=train.target_names)
plt.xlabel('true label')
plt.ylabel('predicted label');

from sklearn.metrics import confusion_matrix  #TF-ID 
mat1 = confusion_matrix(test.target, labels1)
sns.heatmap(mat1.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=train.target_names, yticklabels=train.target_names)
plt.xlabel('true label')
plt.ylabel('predicted label');

def predict_category(s, train=train, model=model): #count
    pred = model.predict([s]) 
    return train.target_names[pred[0]]

predict_category("can ı buy a vehicle with bitcoin?") #count

predict_category("can ı buy a vehicle with bitcoin?", train=train, model=model1) #TF-ID

from sklearn.metrics import accuracy_score #count
print(accuracy_score(test.target, labels))

from sklearn.metrics import accuracy_score #TF-ID
print(accuracy_score(test.target, labels1))

"""BELİRLEDİĞİM KATEGORİLER BAZINDA COUNT VECTORTÜ DAHA BAŞARILI SONUÇ VERDİ MULTİNOMİAL NAİVE MODELDE."""