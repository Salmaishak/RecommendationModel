import numpy as np
import pandas as pd
from collections import Counter


def unique(list1):
    x = np.array(list1)
    # print(np.unique(x))
    # print("length of unique values : ")
    # print(len(np.unique(x)))



attractions = pd.read_csv("attractions.csv", encoding= "latin1")

#getting unique categories
# print("Unique categorues")
categories_list = list(attractions["attraction_type"])
# print("the unique values from 1st list is")
unique(categories_list)

#counting unique amenities
counter_count_of_categories = Counter(categories_list)
# print(counter_count_of_categories)
#sorting unique amenities
# print("most common")
# print(counter_count_of_categories.most_common())
