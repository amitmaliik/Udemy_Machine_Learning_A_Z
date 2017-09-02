# -*- coding: utf-8 -*-
"""
@author: akshay.lagandula
"""
# Data Processing - Template
# Template to use in further exercises

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import Datasets
dataset = pd.read_csv("Data.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Splitting the dataset into the Training set and Train set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
