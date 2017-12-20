""" Currency rate monitor and predictor for BNR course """
import requests
from bs4 import BeautifulSoup
import pickle
import pandas as pd 
import datetime
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
from matplotlib import style
from numpy.lib.function_base import range

mem = {}

try:
    pickle_in = open('cupro.pickle', 'rb')
#except FileNotFoundError as e:
except :     
    print ("Initial Data not found")
    mem = {"nrMonezi": 0}
else:    
    mem = pickle.load(pickle_in)

if not 'last_date' in mem.keys():
    mem["last_date"] = '2005-01-01'
if not 'monezi' in mem.keys():
    mem["monezi"] = {}

dates = []    
today = datetime.datetime.now().strftime("%Y-%m-%d") 
if today > mem["last_date"]:
    try:
        r = requests.get("https://www.cursbnr.ro/arhiva-curs-bnr"
            , proxies=dict(http="http://cna:6yuiop[]@192.168.1.29:8080", https="https://cna:6yuiop[]@192.168.1.29:8080")
            )
    except ConnectionError as e:
        print ("HTTP Connection Error")
        r = None
    
    if not r == None:
        if r.status_code == 200:  # Success
            soup = BeautifulSoup(r.text, "html.parser")
            for tag_date in soup.find_all("a", "arhiva_btn"):
                date = tag_date.attrs['href'][16:]
                if date > mem["last_date"]:
                    dates.append(date)

dates.sort()    
for datex in dates:
    try:
        r = requests.get("https://www.cursbnr.ro/arhiva-curs-bnr-"+datex
            , proxies=dict(http="http://cna:6yuiop[]@192.168.1.29:8080", https="https://cna:6yuiop[]@192.168.1.29:8080")
            )
    except ConnectionError as e:
        print ("HTTP Connection Error")
        r = None
        break;
    
    if not r == None:
        if r.status_code == 200:  # Success
            soup = BeautifulSoup(r.text, "html.parser")
            for table in soup.find_all("table", "table-striped-archive"):
                for row in  table.find_all("tr"):
                    heads=row.find_all("th")
                    cells = row.find_all("td")
                    if len(heads) > 0:
                        date = datex
                    elif len(cells) > 0:
                        symb = cells[0].text
                        den = cells[1].text
                        val = float(cells[2].text)
                        inc = float(cells[3].text)
                        
                        if symb in mem["monezi"].keys():
                            m = mem["monezi"][symb]
                            c=m["info"]
                            d=m["data"]
                            if "Predicts" in d.keys():
                                del d["Predicts"]
                        else:
                            d={'Data': [], 'Valoare': [], "Crestere":[]}
                            c={'idx':0, 'Simbol':symb, 'Name':den, 'Country':'', 'Data_from':date, 'Data_to':date, 'days_predicted':1, 'spread':0, 'success_rate':0, 'max_devia_allow':0, 'avg_devia':0}
                            m = {"info":c, "data":d}
                            mem["monezi"][symb] = m
                        if not "Predicts" in m.keys():
                            m["Predicts"] = []
                            
                        d["Data"].append(date)
                        d["Valoare"].append(val)
                        d["Crestere"].append(inc)
                        c["Data_to"] = date
            mem["last_date"] = datex

df = pd.DataFrame.from_dict(mem["monezi"]['EUR']['data'])
df.set_index("Data", inplace=True)

days_to_learn = 7             #learn to predict a number of days is the future
step_back = 8
predictions = 4

forecast_col = "Valoare";
df=df[["Valoare","Crestere"]]
df.fillna(-99999, inplace = True)
df["label"] = df[forecast_col].shift(-days_to_learn)  # Value in the future 7 days

x = np.array(df.drop(['label'], 1))  # columns without label 
y = np.array(df['label'])            # array from column label

x = preprocessing.scale(x)

style.use('ggplot')
plt.plot(df.index.tolist(),df['Valoare'].tolist(),"blue")

for step in range(predictions):
    days_to_predict = days_to_learn + step_back*step
    x_lately = x[-days_to_predict:]
    x = x[:-days_to_predict]

    d = np.array ( df.index.values )
    d = d[-days_to_predict:]

    df.dropna(inplace=True)
    y = np.array(df['label'])  

    x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.1) # shuffle and use 20% data as test data 

    clf = LinearRegression()
    clf.fit(x_train, y_train)

    forecast_set = clf.predict(x_lately)

    prediction = {"data":[], "val":[]}
    for i in range(len(forecast_set) - 1):
        prediction["data"].append(d[i])
        prediction["val"].append(forecast_set[i])

    plt.plot(prediction["data"],prediction["val"],"red")
plt.show()

with open('cupro.pickle', 'wb') as f:
    pickle.dump(mem, f)
    