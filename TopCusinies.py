import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import math
import numpy as np
from collections import Counter
from collections import defaultdict

giza = pd.read_csv(r'G:\Fourth Year\GP\RecommendationModel\restaurants data\restaurants_giza.csv')
alex = pd.read_csv(r'G:\Fourth Year\GP\RecommendationModel\restaurants data\restaurants_data_alex2.csv')
sharm = pd.read_csv(r'G:\Fourth Year\GP\RecommendationModel\restaurants data\restaurants_data_sharm.csv')
luxor = pd .read_csv(r'G:\Fourth Year\GP\RecommendationModel\restaurants data\Luxor.csv')
cairo = pd .read_csv(r'G:\Fourth Year\GP\RecommendationModel\restaurants data\Cairo_Final.csv')
Alfayyum = pd .read_csv(r'G:\Fourth Year\GP\RecommendationModel\restaurants data\Alfayyum.csv')
Hurghada = pd .read_csv(r'G:\Fourth Year\GP\RecommendationModel\restaurants data\Hurghada.csv')


hash_map=dict()
for cusinie in giza['cuisines']:
    try:
        if cusinie != 'None':
            words = cusinie.split(", ")
            # print(words)
            for word in words:
                # print(word)
                if word in hash_map:
                    hash_map[word]+=1
                else:
                    hash_map[word]=1
                # if hash_map[word] == None:
                #     hash_map[word] = 1
                # else:
                #     hash_map[word] = hash_map[word] + 1
    except:
        ctr=0
        # print("error")
for cusinie in alex['cuisines']:
    try:
        if cusinie != 'None':
            words = cusinie.split(", ")
            # print(words)
            for word in words:
                # print(word)
                if word in hash_map:
                    hash_map[word]+=1
                else:
                    hash_map[word]=1
                # if hash_map[word] == None:
                #     hash_map[word] = 1
                # else:
                #     hash_map[word] = hash_map[word] + 1
    except:
        ctr=0
        # print("error")
for cusinie in sharm['cuisines']:
    try:
        if cusinie != 'None':
            words = cusinie.split(", ")
            # print(words)
            for word in words:
                # print(word)
                if word in hash_map:
                    hash_map[word]+=1
                else:
                    hash_map[word]=1
                # if hash_map[word] == None:
                #     hash_map[word] = 1
                # else:
                #     hash_map[word] = hash_map[word] + 1
    except:
        ctr=0
        # print("error")

for cusinie in luxor['cuisines']:
    try:
        if cusinie != 'None':
            words = cusinie.split(", ")
            # print(words)
            for word in words:
                # print(word)
                if word in hash_map:
                    hash_map[word]+=1
                else:
                    hash_map[word]=1
                # if hash_map[word] == None:
                #     hash_map[word] = 1
                # else:
                #     hash_map[word] = hash_map[word] + 1
    except:
        ctr=0
        # print("error")

for cusinie in cairo['cuisines']:
    try:
        if cusinie != 'None':
            words = cusinie.split(", ")
            # print(words)
            for word in words:
                # print(word)
                if word in hash_map:
                    hash_map[word]+=1
                else:
                    hash_map[word]=1
                # if hash_map[word] == None:
                #     hash_map[word] = 1
                # else:
                #     hash_map[word] = hash_map[word] + 1
    except:
        ctr=0
        # print("error")
for cusinie in Alfayyum['cuisines']:
    try:
        if cusinie != 'None':
            words = cusinie.split(", ")
            # print(words)
            for word in words:
                # print(word)
                if word in hash_map:
                    hash_map[word]+=1
                else:
                    hash_map[word]=1
                # if hash_map[word] == None:
                #     hash_map[word] = 1
                # else:
                #     hash_map[word] = hash_map[word] + 1
    except:
        ctr=0
        # print("error")

for cusinie in Hurghada['cuisines']:
    try:
        if cusinie != 'None':
            words = cusinie.split(", ")
            # print(words)
            for word in words:
                # print(word)
                if word in hash_map:
                    hash_map[word]+=1
                else:
                    hash_map[word]=1
                # if hash_map[word] == None:
                #     hash_map[word] = 1
                # else:
                #     hash_map[word] = hash_map[word] + 1
    except:
        ctr=0
        # print("error")

# print(hash_map)
# for x,value in hash_map.items():
#     print(x,value)
    # print(x.value)
# print("Sorted")
# print(sorted(hash_map))

sorted_dict = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))

print(sorted_dict)