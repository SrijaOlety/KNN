# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 10:36:14 2023

@author: dell
"""


#zoo
#importing the data
import numpy as np
import pandas as pd
df = pd.read_csv("D:\\data science python\\NEW DS ASSESSMENTS\\Zoo.csv")
df
df.info()

#data split and transform
X_trans = df.iloc[:,1:17]
X_trans
list(X_trans)
from sklearn.preprocessing import StandardScaler
SS = StandardScaler()
SS_X = SS.fit_transform(X_trans)
SS_X
X = pd.DataFrame(SS_X)
X.columns = list(X_trans)
X

#for y variable
from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
df_sep = df[df.columns[[17]]]
df_sep
df_sep.iloc[:,0] = LE.fit_transform(df_sep.iloc[:,0])
df_sep
Y = df_sep.iloc[:,0] = LE.fit_transform(df_sep.iloc[:,0])
Y

#data partition
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size=0.75,random_state=4)
X_train
X_test
Y_train
Y_test

#model fitting KNN
from sklearn.neighbors import KNeighborsClassifier
KNN = KNeighborsClassifier(n_neighbors=5,p=2)
KNN.fit(X_train,Y_train)
Y_pred_train = KNN.predict(X_train)
Y_pred_train 
Y_pred_test = KNN.predict(X_test)
Y_pred_test

#metrics
from sklearn.metrics import accuracy_score
AC1 = accuracy_score(Y_train,Y_pred_train)
print("Training Accuracy score : ",AC1.round(3))
AC2 = accuracy_score(Y_test,Y_pred_test)
print("Testing Accuracy score : ",AC2.round(3))

#cross validation (validation set approach)
l1 = []
l2 = []

training_accuracy = []
testing_accuracy = []

for i in range(1,100):
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size=0.75,random_state=i)
    KNN = KNeighborsClassifier(n_neighbors=13,p=2)
    KNN.fit(X_train,Y_train)
    Y_pred_train = KNN.predict(X_train)
    Y_pred_test = KNN.predict(X_test)
    training_accuracy.append(accuracy_score(Y_train,Y_pred_train))
    testing_accuracy.append(accuracy_score(Y_test,Y_pred_test))
   
import numpy as np
print("Average training error : ",np.mean(training_accuracy).round(3))
print("Average testing error : ",np.mean(testing_accuracy).round(3))

# k = 5,7,9,11,13
l1.append(np.mean(training_accuracy).round(3))
l2.append(np.mean(testing_accuracy).round(3))
print(l1)
print(l2)

#plot to know which point is nearest
import matplotlib.pyplot as plt
plt.scatter(range(5,15,2),l1)
plt.plot(range(5,15,2),l1,color='black')
plt.scatter(range(5,15,2),l2,color="red")
plt.plot(range(5,15,2),l2,color='black')
plt.show()

#-->therefore the accuracies were better when n_neighbour = 11 



# Glass( SECOND DATASET )

#importing the data
import numpy as np
import pandas as pd
df = pd.read_csv("D:\\data science python\\NEW DS ASSESSMENTS\\KNN\\glass (1).csv")
df

#data split and transform
X_trans = df.iloc[:,0:9]
X_trans
list(X_trans)
from sklearn.preprocessing import StandardScaler
SS = StandardScaler()
SS_X = SS.fit_transform(X_trans)
SS_X
X = pd.DataFrame(SS_X)
X.columns = list(X_trans)
X

#for y variable
from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
df_sep = df[df.columns[[9]]]
df_sep
df_sep.iloc[:,0] = LE.fit_transform(df_sep.iloc[:,0])
df_sep
Y = df_sep.iloc[:,0] = LE.fit_transform(df_sep.iloc[:,0])
Y

#data partition
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size=0.75,random_state=4)
X_train
X_test
Y_train
Y_test

#model fitting KNN
from sklearn.neighbors import KNeighborsClassifier
KNN = KNeighborsClassifier(n_neighbors=5,p=2)
KNN.fit(X_train,Y_train)
Y_pred_train = KNN.predict(X_train)
Y_pred_train 
Y_pred_test = KNN.predict(X_test)
Y_pred_test

#metrics
from sklearn.metrics import accuracy_score
AC1 = accuracy_score(Y_train,Y_pred_train)
print("Training Accuracy score : ",AC1.round(3))
AC2 = accuracy_score(Y_test,Y_pred_test)
print("Testing Accuracy score : ",AC2.round(3))

#cross validation (validation set approach)
l1 = []
l2 = []

training_accuracy = []
testing_accuracy = []

for i in range(1,100):
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size=0.75,random_state=i)
    KNN = KNeighborsClassifier(n_neighbors=13,p=2)
    KNN.fit(X_train,Y_train)
    Y_pred_train = KNN.predict(X_train)
    Y_pred_test = KNN.predict(X_test)
    training_accuracy.append(accuracy_score(Y_train,Y_pred_train))
    testing_accuracy.append(accuracy_score(Y_test,Y_pred_test))
   
import numpy as np
print("Average training error : ",np.mean(training_accuracy).round(3))
print("Average testing error : ",np.mean(testing_accuracy).round(3))

# k = 5,7,9,11,13
l1.append(np.mean(training_accuracy).round(3))
l2.append(np.mean(testing_accuracy).round(3))
print(l1)
print(l2)

#plot to know which point is nearest
import matplotlib.pyplot as plt
plt.scatter(range(5,15,2),l1)
plt.plot(range(5,15,2),l1,color='black')
plt.scatter(range(5,15,2),l2,color="red")
plt.plot(range(5,15,2),l2,color='black')
plt.show()

#-->therefore the accuracies were better when n_neighbour = 13