import pandas as pd
import quandl
import numpy as np
import math
import datetime
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression   
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

df = quandl.get('WIKI/GOOGL')  # get historic of a stock

# print(df.head(5))

df = df[["Adj. Open","Adj. High","Adj. Low","Adj. Close","Adj. Volume"]]

df["HL_PCT"] = ((df["Adj. High"] - df["Adj. Close"]) / df["Adj. Close"]) * 100     # High / Close Percentage
df["PCT_change"] = ((df["Adj. Close"] - df["Adj. Open"]) / df["Adj. Open"]) * 100  # Close/Open Precentage

df=df[["Adj. Close","HL_PCT","PCT_change","Adj. Volume"]]

# print (df.head())

forecast_col = "Adj. Close";
df.fillna(-99999, inplace = True)

forecast_out = int(math.ceil(0.01*len(df)))
# print ("forecast_out =" + str(forecast_out))

df["label"] = df[forecast_col].shift(-forecast_out)  # Value in the future (1% of the whole period) ~ 34 days

print (df.head(10))

x = np.array(df.drop(['label'], 1))  # columns without label 
y = np.array(df['label'])            # array from column label

print (x)
print (y)

x = preprocessing.scale(x)
x_lately = x[-forecast_out:]
x = x[:-forecast_out]

df.dropna(inplace=True)
y = np.array(df['label'])  

print (x)
print (y)

x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.2) # shuffle and use 20% data as test data 

clf = LinearRegression()
clf.fit(x_train, y_train)
accuracy =  clf.score(x_test, y_test)

forecast_set = clf.predict(x_lately)

print (forecast_set, accuracy, forecast_out )
