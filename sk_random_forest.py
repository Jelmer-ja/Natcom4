# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:14:16 2018

@author: tpayer
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import svm
import pandas as pd
import numpy as np


wine_quality = pd.read_csv("./winequality-white.csv", delimiter= ";")
wine_quality_predictors = np.asanyarray(wine_quality.iloc[:,0:11])
wine_quality_target = np.asanyarray(wine_quality.iloc[:,11])

#%% cross- validation
X_train, X_test, y_train, y_test = train_test_split(
    wine_quality_predictors, wine_quality_target, test_size=0.4, random_state=0)

#%%

clf = RandomForestClassifier(max_depth=100, random_state=0)
clf.fit(X_train, y_train)

# Sepal Length, Sepal Width, Petal Length and Petal Width
importances = clf.feature_importances_
#predictions = clf.predict(X)

print(importances)
print(clf.score(X_test, y_test))

#%%
'''
accuracy = []
for depth in range(2,31):
    clf = RandomForestClassifier(max_depth=depth, random_state=0).fit(X_train, y_train)
    accuracy.append(clf.score(X_test, y_test))

#%%
SVM = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
SVM.score(X_test, y_test)     
'''