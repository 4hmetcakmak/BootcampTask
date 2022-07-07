# -*- coding: utf-8 -*-
"""CEV VBE Ch-4 ExercisesTasks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KsCeDsL8VHia206JeQT4Vbm6teK_vULb
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import seaborn as sns                       #visualisation
import matplotlib.pyplot as plt             #visualisation
# %matplotlib inline     
sns.set(color_codes=True)
#https://colab.research.google.com/drive/1WBLs7Hq3k4TgJV1Ym_CglYVI6ZKiReDx#scrollTo=GGyDovL2QDLa buna bakabilirsin

"""TASK-A: Please download the dataset and upload it to Colab environment. Then check the dataset (head and tail) after reading the dataset. """

mall=pd.read_csv("/content/Mall_Customers (4).csv")
mall.head()
mall.tail(5)

"""TASK-B: Please check the descriptive statistics of this dataset by the use of describe function."""

mall.describe()

"""TASK-C: Please provide a control for the missing values and report your findings very briefly."""

mall.isnull().sum()

"""TASK-D: Please check and clean the dataset regarding the potential outliers by the use of IQR method and report your findings accordingly. """

sns.boxplot(mall["Spending Score (1-100)"])

sns.boxplot(df["Annual Income (k$)"])

q1=mall.quantile(0.25)
q3=mall.quantile(0.75)
IQR= q3-q1
IQR
df = mall[~((mall < (q1 - 1.5 * IQR)) |(mall > (q3 + 1.5 * IQR))).any(axis=1)]

"""TASK-E: Please provide a correlation analysis for the columns and demonstrate it via heatmap."""

plt.figure(figsize=(10,5))
c=df.corr()
sns.heatmap(c, cmap="BrBG",annot=True)

"""TASK-F: Please provide histrograms for each of the columns and briefly write down your observations. """

df.hist(bins=40, figsize=(10, 5))

"""TASK-G: Please provide a pairplot from the Seaborn library for understanding the relationship between columns."""

sns.pairplot(df);

"""TASK-H: Please provide a comprehensive analysis by the use of a scatter plot with getting the possible contributions from color and size parameters."""

fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['Spending Score (1-100)'], df['Annual Income (k$)'], c=df["Age"], s=df["CustomerID"])
ax.set_xlabel('Spending Score (1-100)')
ax.set_ylabel('Annual Income (k$)')
plt.show()

"""TASK-I: Please provide a pivot table for the following analyses:
- Gender based analysis (Female or Male)
- Age based analysis (Quartiles: 4 groups)
- Annual income (higher/lower than median)
- Spending score (higher/lower than median)
Your table should include the counts of these mall customers regarding the distributions given above.

"""

df.pivot_table("Annual Income (k$)", index="Gender", columns="Age")

age = pd.qcut(df['Age'], 4)
df.pivot_table('Spending Score (1-100)',index=["Gender",age], aggfunc= "count" )

annual=pd.qcut(df["Annual Income (k$)"],2 )
spending=pd.qcut(df["Spending Score (1-100)"], 2)
df.pivot_table('Spending Score (1-100)',index=["Gender",age], columns= [annual, spending], aggfunc= "count" )

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
sns.set()  # use Seaborn styles
df.pivot_table('Spending Score (1-100)',index=["Gender",age], columns= [annual, spending], aggfunc= "count" ).plot(kind="bar", figsize=(10,6))
plt.ylabel("Spending score for variable")