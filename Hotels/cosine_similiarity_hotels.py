import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
all_hotels = pd.read_csv("Allhotels.csv", encoding='latin1')



def get_recommendation(hotel_name):

    count_vectorizer = CountVectorizer()
    count_matrix = count_vectorizer.fit_transform(all_hotels["amenities"].apply(lambda count_matrix: np.str_(count_matrix)))


    cosine_sim = cosine_similarity(count_matrix)
    hotel_index = get_index_from_hotelName(hotel_name)

    similar_hotels = list(enumerate(cosine_sim[hotel_index]))

    sorted_similar_hotels = sorted(similar_hotels, key=lambda x: x[1], reverse=True)

    city = get_city_from_hotelName(hotel_name)


    i = 0
    for hotel in sorted_similar_hotels:
        name_of_hotel = get_hotelName_from_index(hotel[0])
        if( name_of_hotel == hotel_name):
            continue
        if (get_city_from_hotelName(name_of_hotel) != city):
            continue
        print(print_hotel_details(name_of_hotel))


        i = i + 1
        if (i == 3):
            break

def get_index_from_hotelName(name):
    return all_hotels[all_hotels.name == name]["hotelID"].values[0]

def get_city_from_hotelName(name):
    return all_hotels[all_hotels.name == name]["City"].values[0]

def get_hotelName_from_index(index):
    return all_hotels[all_hotels.hotelID == index]["name"].values[0]

def print_hotel_details(name):
    return all_hotels[all_hotels.name == name]["name"].values[0],all_hotels[all_hotels.name == name]["ratings"].values[0],all_hotels[all_hotels.name == name]["Price Range"].values[0]

#print(pp("Fort Arabesque Resort, Spa & Villas"))
get_recommendation("Fort Arabesque Resort, Spa & Villas")


