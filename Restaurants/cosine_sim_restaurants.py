import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity
df = pd.read_csv("Allrestaurants.csv", encoding='latin1')

#print(df.head())

df["cuisines"].fillna("", inplace=True)

cv = CountVectorizer(stop_words='english')
count_matrix = cv.fit_transform(df["cuisines"])
#print("Count Matrix:", count_matrix.toarray())
#print(cv.get_stop_words(count_matrix))
#print(cv.get_feature_names_out(count_matrix))
# compute the cosine similarity matrix
similarity = cosine_similarity(count_matrix)
#print(similarity)



# create a function that takes in restaurant name as input and returns a list of the most similar restaurants
def get_recommendations(RestaurantName, n, cosine_sim=similarity):
    # get the index of the restaurants that matches the restaurant name
    restaurant_index = df[df.Name == RestaurantName].index.values[0]

    # get the pairwsie similarity scores of all restaurants with that restaurant and sort the restaurant based on the similarity scores
    sim_scores_all = sorted(list(enumerate(cosine_sim[restaurant_index])), key=lambda x: x[1], reverse=True)

    # checks if recommendations are limited
    if n > 0:
        sim_scores_all = sim_scores_all[1:n + 1]

    # get the restaurant indices of the top similar restaurants
    restaurants_indices = [i[0] for i in sim_scores_all]
    scores = [i[1] for i in sim_scores_all]
    for i in restaurants_indices:
        print( i)
    # return the top n most similar restaurants from the restaurants df
    top_restaurants = pd.DataFrame(df.iloc[restaurants_indices]['Name'])
    top_restaurants['sim_scores'] = scores
    top_restaurants['ranking'] = range(1, len(top_restaurants) + 1)
    return top_restaurants, sim_scores_all


# generate a list of recommendations for a specific restaurant name
restaurant_name = 'Beeja'
top_restaurants_df, _ = get_recommendations(restaurant_name, 20)



