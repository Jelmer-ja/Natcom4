# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 15:04:12 2018

@author: tpaye
"""

from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np


wine_quality = pd.read_csv("./winequality-white.csv", delimiter= ";")
wine_quality_predictors = np.asanyarray(wine_quality.iloc[:,0:11])
wine_quality_target = np.asanyarray(wine_quality.iloc[:,11])

#%% cross- validation
X_train, X_test, y_train, y_test = train_test_split(
    wine_quality_predictors, wine_quality_target, test_size=0.4, random_state=0)

#%% AdaBoost classifier

clf_1 = DecisionTreeClassifier(max_depth=20)

clf_2 = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1),
                          n_estimators=600, algorithm="SAMME", random_state=0)

clf_1.fit(X_train, y_train)
clf_2.fit(X_train, y_train)

print(clf_1.score(X_test, y_test))
print(clf_2.score(X_test, y_test))

#%%
'''
accuracy = []
for estimators in range(1,50):
    clf = AdaBoostClassifier(n_estimators=estimators, random_state=0).fit(X_train, y_train)
    accuracy.append(clf.score(X_test, y_test))
    
print(accuracy)
'''