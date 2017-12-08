import os
print(os.listdir())
# pip install pandas
# pip install ipython
# pip install jupyter
#  jupyter notebook
# pip install xlrd    (for pandas.read_excel())

import numpy
n=numpy.arange(27)

print(n)
print(n.reshape(3,9))
print(n.reshape(3,3,3))

import pandas
df=pandas.read_csv("supermarkets.csv") # ,header=None
df.set_index("ID")
print(df)

df=pandas.read_json("supermarkets.json") # ,header=None
print(df)

df=pandas.read_excel("supermarkets.xlsx",sheet_name=0)
print(df)

df7=df
df7=df.set_index("Address")
print( df7.loc["735 Dolores St":"3995 23rd St","City":"Country"] )

print( df7.iloc[1:3,1:3] )

print (df7.ix[1:3,"City":"Country"])

df7.drop("735 Dolores St",0)  # ,1 for columns

df7["Continent"] = df7.shape[0] * ["North America"]
df7["Continent"] = df7["Country"] + ", " + "North America"
print(df7)


from geopy.geocoders import Nominatim
nom=Nominatim(scheme="http")
n=nom.geocode("1 Calea Apeductului, Bucharest, Romania")
print(n)
print(n.latitude)
print(n.longitude)

df7 = pandas.read_csv("supermarkets.csv")
df7["FullAddress"] = df7["Address"] + ", " + df7["City"] + ", " + df7["State"] + ", " + df7["Country"]
df7["Coord"] = df7["FullAddress"].apply(nom.geocode)
df7["Latitude"] = df7["Coord"].apply(lambda x: x.latitude if x != None else None)
df7["Longitude"] = df7["Coord"].apply(lambda x: x.longitude if x != None else None)
print(df7)


# pip install opencv-python
# pip install ipykernel
# python -m ipykernel install --user --name=venv_dml

import cv2
im_g = cv2.imread("smallgray.png",0)  # gray BGR values from 0 to 255  (not RGB)
print(im_g) 

im_g = cv2.imread("smallgray.png",1) # 3D array with R, G and B layers, transposed
print(im_g)

cv2.imwrite("newsmallgray.png",im_g)

im_g = cv2.imread("smallgray.png",0)
print(im_g[0:2,2:4])

for i in im_g:
    print(i)
for i in im_g.T:
    print(i)
for i in im_g.flat:
    print(i)
    
imh = numpy.hstack((im_g,im_g))
print(imh)
imv = numpy.vstack((im_g, im_g))
print(imv)
lsth = numpy.hsplit(imh, 2)  # slice in 3 pieces, horizontally
print(lsth)
lstv = numpy.vsplit(imv, 3)
print(lstv)


#from bs4 import BeautefulSoup
# import requests
# 
# r=requests.get("https://en.wikipedia.org/wiki/Eagle")
# print(r.content)
