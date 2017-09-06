# -*- coding: utf-8 -*-
"""

@author: akshay.lagandula
"""

# Simple Linear Regression

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import Datasets
dataset = pd.read_csv("Salary_Data.csv")
X = dataset.iloc[:, 0].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Train set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fitting SLR to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# If you encounter any value-error regarding dimensions of the arrays
# y_train = y_train.reshape(20,1)
# y_test = y_test.reshape(10,1)
# X_train = X_train.reshape(20,1)
# X_test = X_test.reshape(10,1)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Visualising the training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_test, regressor.predict(X_test), color = 'blue')
plt.title('Salary vs Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()