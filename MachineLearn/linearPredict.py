import pandas as pd
import quandl
import numpy as np
import math
import datetime
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression   
import matplotlib.pyplot as plt 
from matplotlib import style
import pickle

style.use('ggplot')

df = quandl.get('WIKI/GOOGL')  # get historic of a stock

df["HL_PCT"] = ((df["Adj. High"] - df["Adj. Close"]) / df["Adj. Close"]) * 100     # High / Close Percentage
df["PCT_change"] = ((df["Adj. Close"] - df["Adj. Open"]) / df["Adj. Open"]) * 100  # Close/Open Precentage
df=df[["Adj. Close","HL_PCT","PCT_change","Adj. Volume"]]

forecast_col = "Adj. Close";        # the real value 
df.fillna(-99999, inplace = True)
forecast_out = int(math.ceil(0.01*len(df)))

df0 = df[["Adj. Close","HL_PCT","PCT_change","Adj. Volume"]]  # keep a copy of original data
df = df[:-forecast_out]                                       # remove the last days                    
 
df["label"] = df[forecast_col].shift(-forecast_out)  # Value in the future (1% of the whole period) ~ 34 days
                                                     # so we are training the machine to predict 34 days in the future
print (forecast_out, df.tail(50))

x = np.array(df.drop(['label'], 1))  # columns without label 
y = np.array(df['label'])            # array from column label

x = preprocessing.scale(x)           # scaling
x_lately = x[-forecast_out:]         # remove rows without training data
x = x[:-forecast_out]
df.dropna(inplace=True)              # remove rows without training data
y = np.array(df['label'])  

clf = LinearRegression()             
clf.fit(x, y)                        # machine learn self train to model the known behave
forecast_set = clf.predict(x_lately) # run for last days (untrained input) 

df['Forecast'] = np.nan
d = df0.index.values
dates = d[-forecast_out:]            # these are the days you assume is predicting

# ???????????????????????????????????????????????????????????????????????????????????????????
# dates = d[-forecast_out*2:]        # these are the days that is actually predicting (uncomment to see)
# ???????????????????????????????????????????????????????????????????????????????????????????

for i in range(len(forecast_set)):
    df.loc[dates[i]] = [np.nan for _ in range(len(df.columns)-1)] + [forecast_set[i]]

print(df.tail(50), forecast_set) 
   
df0["Adj. Close"].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()

y = 0  #breakpoint here
