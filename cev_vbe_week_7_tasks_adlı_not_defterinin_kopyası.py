# -*- coding: utf-8 -*-
"""CEV VBE Week#7.Tasks adlı not defterinin kopyası

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r5SpKs_EMqvkM-l9mcOZOhcA2xz3WaC3

LOOPS + FUNCTIONS:

Please write a boolean function that will determine whether a given number is divisible only by three prime numbers.

is_3_primes ( 30) : true
is_3_primes (10 ) : false
"""

#bunu maalesef yapamadım hocaya bu konudaki eksikliğimi bildirdim

"""TASK-7A: Please develop 3 classification models with the use of algorithms other than GaussianNB on iris dataset and compare the model performances in terms of accuracy and confusion matrix.

1. load_iris(): get the dataset
2. Divide iris dataset into two parts: X and y
   Features and labels as separate datasets
3. train-test split (train: 0.7; test: 0.3)
4. Model-1: Support Vector Machine (linear)
   Model-2: DecisionTreeClassifier 
   Model-3: RandomForestClassifier
5. Model development via fit function
6. Model test via predict function
7. Model evaluation via accuracy function
8. Confusion matrix for these three models

Note-1: cross_validation -> model_selection
"""

import seaborn as sns
iris=sns.load_dataset("iris")
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()     
X_iris = iris.drop('species', axis=1)
X_iris.shape
y_iris = iris['species']
y_iris.shape
from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris,
                                                random_state=1, train_size=0.7, test_size=0.3)

# Commented out IPython magic to ensure Python compatibility.
model.fit(Xtrain,ytrain) #classification mdel  #GaussianNB (reference model)
y_model=model.predict(Xtest)
from sklearn.metrics import accuracy_score
print(accuracy_score(ytest, y_model))
from sklearn.metrics import confusion_matrix
mat=confusion_matrix(ytest,y_model)
# %matplotlib inline
import matplotlib.pyplot as plt
sns.set();
sns.heatmap(mat,square=True, annot=True, cbar=False)
plt.xlabel('predicted value')
plt.ylabel('true value');

from sklearn.tree import DecisionTreeClassifier #DecisionTreeClassifier
modela=DecisionTreeClassifier()
modela.fit(Xtrain,ytrain)
y_modela=modela.predict(Xtest)
print(accuracy_score(ytest, y_modela))
mata=confusion_matrix(ytest,y_modela)
sns.heatmap(mata,square=True, annot=True, cbar=False)
plt.xlabel('predicted value')
plt.ylabel('true value');

from sklearn.ensemble import RandomForestClassifier #RandomForestClassifier
modelb= RandomForestClassifier(n_estimators=100, random_state=0)
modelb.fit(Xtrain,ytrain)
y_modelb=modelb.predict(Xtest)
print(accuracy_score(ytest, y_modelb))
matb=confusion_matrix(ytest,y_modelb)
sns.heatmap(matb,square=True, annot=True, cbar=False)
plt.xlabel('predicted value')
plt.ylabel('true value');

#support vector machine
from sklearn.svm import SVC
modelc=SVC()
modelc.fit(Xtrain, ytrain)
y_modelc=modelc.predict(Xtest)
print(accuracy_score(ytest, y_modelc))
matc=confusion_matrix(ytest,y_modelc)
sns.heatmap(matc,square=True, annot=True, cbar=False)
plt.xlabel('predicted value')
plt.ylabel('true value');

"""Yukarıdaki karşılaştırmalara göre çook yakın tahminler olsa da support vector machine algoritması daha doğru tahminler vermektedir.

TASK-7B: Please develop 5 classification models with the use of algorithms other than GaussianNB on digits dataset and compare the model performances in terms of accuracy and confusion matrix.

1. load_iris(): get the dataset
2. Divide iris dataset into two parts: X and y
   Features and labels as separate datasets
3. train-test split (train: 0.7; test: 0.3)
4. Model-1: Support Vector Machine (linear)
   Model-2: DecisionTreeClassifier 
   Model-3: RandomForestClassifier
   Model-4: KNN
   Model-5: GaussianNB (reference model)
5. Model development via fit function
6. Model test via predict function
7. Model evaluation via accuracy function
8. Confusion matrix for these five models

Note-1: cross_validation -> model_selection
"""

from sklearn.datasets import load_digits
digits = load_digits()
X = digits.data
print(X.shape)
y = digits.target
print(y.shape)
y

from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y,
                                                random_state=0, train_size=0.7, test_size=0.3)

from sklearn.naive_bayes import GaussianNB #GaussianNB (reference model)
model = GaussianNB()
model.fit(Xtrain,ytrain)
model_y=model.predict(Xtest)
print(accuracy_score(ytest, model_y))
mat=confusion_matrix(ytest,model_y)
sns.heatmap(mat,square=True, annot=True, cbar=False)
plt.xlabel('predicted value')
plt.ylabel('true value');

#Support Vector Machine (linear)
from sklearn.svm import SVC
modelA=SVC()
modelA.fit(Xtrain, ytrain)
y_modelA=modelA.predict(Xtest)
print(accuracy_score(ytest, y_modelA))
matA=confusion_matrix(ytest,y_modelA)
sns.heatmap(matA,square=True, annot=True, cbar=False)
plt.xlabel('predicted value')
plt.ylabel('true value');

#Model-2: DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
modelB=DecisionTreeClassifier()
modelB.fit(Xtrain,ytrain)
y_modelB=modelB.predict(Xtest)
print(accuracy_score(ytest, y_modelB))
matB=confusion_matrix(ytest,y_modelB)
sns.heatmap(matB,square=True, annot=True, cbar=False)
plt.xlabel('predicted value')
plt.ylabel('true value');

#RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier 
modelC= RandomForestClassifier(n_estimators=100, random_state=0)
modelC.fit(Xtrain,ytrain)
y_modelC=modelC.predict(Xtest)
print(accuracy_score(ytest, y_modelC))
matC=confusion_matrix(ytest,y_modelC)
sns.heatmap(matC,square=True, annot=True, cbar=False)
plt.xlabel('predicted value')
plt.ylabel('true value');

#KNN Model
from sklearn.neighbors import KNeighborsClassifier
modelD= RandomForestClassifier(n_estimators=100, random_state=0)
modelD.fit(Xtrain,ytrain)
y_modelD=modelD.predict(Xtest)
print(accuracy_score(ytest, y_modelD))
matD=confusion_matrix(ytest,y_modelD)
sns.heatmap(matD,square=True, annot=True, cbar=False)
plt.xlabel('predicted value')
plt.ylabel('true value');

"""Bu örnek için ise en iyi olacak algoritma support vector machine ancak KNN model ve Random forest classifier modelleri de iyi tahminlerde bulunabiliyor"""