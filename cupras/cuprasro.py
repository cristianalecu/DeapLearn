""" Currency rate monitor and predictor for BNR course """
import requests
from bs4 import BeautifulSoup
import pickle
import pandas as pd

mem = {}

try:
    pickle_in = open('cupro.pickle', 'rb')
#except FileNotFoundError as e:
except :     
    print ("Initial Data not found")
    mem = {"nrMonezi": 0}
    d={'Data': [], 'Valoare': [], "Crestere":[], "Predicts":[]}
    c={'idx':0, 'Simbol':'', 'Name':'', 'Country':'', 'Data_from':'', 'Data_to':'', 'days_predicted':1, 'spread':0, 'success_rate':0, 'max_devia_allow':0, 'avg_devia':0}
    #df = pd.DataFrame(data=d)
else:    
    mem = pickle.load(pickle_in)

if not 'last_date' in mem.keys():
    mem["last_date"] = '2005-01-01'
if not 'monezi' in mem.keys():
    mem["monezi"] = {}
    
try:
    r = requests.get("https://www.cursbnr.ro/arhiva-curs-bnr-2005-01-03"
        , proxies=dict(http="http://cna:6yuiop[]@192.168.1.29:8080", https="https://cna:6yuiop[]@192.168.1.29:8080")
        )
except ConnectionError as e:
    print ("HTTP Connection Error")
    r = None

if not r == None:
    if r.status_code == 200:  # Success
        soup = BeautifulSoup(r.text, "html.parser")
        for table in soup.find_all("table", "table-striped-archive"):
            d={'Data': [], 'Valoare': [], "Crestere":[], "Predicts":[]}
            c={'idx':0, 'Simbol':'', 'Name':'', 'Country':'', 'Data_from':'', 'Data_to':'', 'days_predicted':1, 'spread':0, 'success_rate':0, 'max_devia_allow':0, 'avg_devia':0}
            for row in  table.find_all("tr"):
                heads=row.find_all("th")
                cells = row.find_all("td")
                if len(heads) > 0:
                    date = heads[2].text
                elif len(cells) > 0:
                    symb = cells[0].text
                    den = cells[1].text
                    val = cells[2].text 
                    inc = cells[3].text
            m = {"info":c, "data":d}        
            mem["monezi"].append(m)
        
with open('cupro.pickle', 'wb') as f:
    pickle.dump(mem, f)
    