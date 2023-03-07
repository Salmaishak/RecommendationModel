import pandas as pd
import  matplotlib as plt
import matplotlib.pyplot as plt
import math
import numpy as np
from collections import Counter
from collections import defaultdict


fayoum = pd.read_csv('C:\\Users\\rawan\\Documents\\Hotels Data\\HotelsFayoum.csv')
giza = pd.read_csv('C:\\Users\\rawan\\Documents\\Hotels Data\\HotelsGiza.csv')
luxor = pd.read_csv('C:\\Users\\rawan\\Documents\\Hotels Data\\HotelsLuxor.csv')
hurghada = pd.read_csv('C:\\Users\\rawan\\Documents\\Hotels Data\\HotelsHurgada.csv')
sharm = pd.read_csv('C:\\Users\\rawan\\Documents\\Hotels Data\\HotelsSharm.csv')
cairo = pd.read_csv('C:\\Users\\rawan\\Documents\\Hotels Data\\HotelsCairo.csv')
alex = pd.read_csv('C:\\Users\\rawan\\Documents\\Hotels Data\\HotelsAlexandria.csv',encoding='latin1')
allhotels = pd.read_csv('C:\\Users\\rawan\\Documents\\Hotels Data\\Allhotels.csv')


def unique(list1):
    x = np.array(list1)
    print(np.unique(x))
    print("length of unique values : ")
    print(len(np.unique(x)))

amenities_list=[]
for ind, row in allhotels.iterrows():


   if (pd.isna(row[4])):
        continue

   amenities = row[4]
   row_amenities = amenities.split(",")

   amenities_list = np.concatenate((amenities_list, row_amenities))


   #print('\n') # Use the escape character '\n' to print an empty new line.



#getting unique amenities
print("Unique Amenities")
listt = amenities_list.tolist()
print("the unique values from 1st list is")
unique(listt)

#counting unique amenities
counter_count_of_amenities = Counter(listt)
print(counter_count_of_amenities)
#sorting unique amenities
print("most common")
print(counter_count_of_amenities.most_common())

#print(amenities_list.tolist())