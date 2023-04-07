# -*- coding: utf-8 -*-
"""credit

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fVk06_lzAEZ4xPEve7nVrW4qJlriNC3n
"""



"""Importing the dependencies"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#loading the dataset to a pandas data frame
credit_card_data=pd.read_csv('/content/creditcard.csv')

#first 5 rows of data set
credit_card_data.head()

#dataset information
credit_card_data.info()

#checking the number of missing values in each column
credit_card_data.isnull().sum()

#distribution of logit transactions & fradulent transactions
credit_card_data['Class'].value_counts()

"""this dataset is higly unbalanced

0-->Normal transaction
1-->fradulent transaction
"""

#separating the data for analysis
legit = credit_card_data[credit_card_data.Class == 0]
fraud=credit_card_data[credit_card_data.Class == 1]

print(legit.shape)
print(fraud.shape)

#statistical measures of data
legit.Amount.describe()

fraud.Amount.describe()

#compare the values for both transactions
credit_card_data.groupby('Class').mean()

"""undersampling

build a sample dataset containing similar distribution of normal transactions and fradulent transactions

number of fradulent transactions ->103
"""

legit_sample = legit.sample(n=103)

"""concatenating two Dataframes"""

new_dataset = pd.concat([legit_sample, fraud], axis=0)

new_dataset.head()

new_dataset.tail()

new_dataset['Class'].value_counts()

new_dataset.groupby('Class').mean()

"""splitting the data into features and targets"""

X = new_dataset.drop(columns='Class', axis=1)
Y = new_dataset['Class']

print(X)

print(Y)

"""splitting the data into training and testing data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""model training

Logistic regression
"""

model = LogisticRegression()

#training the logisticregression model with training data
model.fit(X_train, Y_train)

"""model evaluation and accuracy score"""

#accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accutracy on Training data :', training_data_accuracy)

#accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy score on test data :', test_data_accuracy)

