import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity
df = pd.read_csv("attractions.csv", encoding='latin1')

print(df.head())


cv = CountVectorizer(stop_words='english')
count_matrix = cv.fit_transform(df["keywords"])
print("Count Matrix:", count_matrix.toarray())
#print(cv.get_stop_words(count_matrix))
print(cv.get_feature_names_out(count_matrix))
# compute the cosine similarity matrix
similarity = cosine_similarity(count_matrix)
print(similarity)



# create a function that takes in attraction name as input and returns a list of the most similar attractions
def get_recommendations(attractionName, n, cosine_sim=similarity):
    # get the index of the attraction that matches the attraction name
    attraction_index = df[df.attraction_name == attractionName].index.values[0]
    print(attraction_index, attractionName)

    # get the pairwsie similarity scores of all movies with that movie and sort the movies based on the similarity scores
    sim_scores_all = sorted(list(enumerate(cosine_sim[attraction_index])), key=lambda x: x[1], reverse=True)

    # checks if recommendations are limited
    if n > 0:
        sim_scores_all = sim_scores_all[1:n + 1]

    # get the attraction indices of the top similar attractions
    attraction_indices = [i[0] for i in sim_scores_all]
    scores = [i[1] for i in sim_scores_all]

    # return the top n most similar movies from the movies df
    top_attractions_df = pd.DataFrame(df.iloc[attraction_indices]['attraction_name'])
    top_attractions_df['sim_scores'] = scores
    top_attractions_df['ranking'] = range(1, len(top_attractions_df) + 1)

    return top_attractions_df, sim_scores_all


# generate a list of recommendations for a specific attraction name
attraction_name = 'The Hanging Church'
number_of_recommendations = 15
top_attractions_df, _ = get_recommendations(attraction_name, number_of_recommendations)

print(top_attractions_df)



# list of attractions a user has liked
attractions_list = ['Abdeen Palace Museum', 'Al-Azhar Park', 'Mosque of Muhammad Ali']

# create a copy of the attractions dataframe and add a column in which we aggregated the scores
user_scores = pd.DataFrame(df['attraction_name'])
user_scores['sim_scores'] = 0.0

# top number of scores to be considered for each attractions
number_of_recommendations = 20
for attraction_name in attractions_list:
    top_attractions_df, _ = get_recommendations(attraction_name, number_of_recommendations)
    # aggregate the scores
    user_scores = pd.concat([user_scores, top_attractions_df[['attraction_name', 'sim_scores']]]).groupby(['attraction_name'], as_index=False).sum({'sim_scores'})

# sort and print the aggregated scores
top_attractions_per_user_df = user_scores.sort_values(by='sim_scores', ascending=False)[1:20]
df = top_attractions_per_user_df[top_attractions_per_user_df.attraction_name.isin(attractions_list) == False]
print(top_attractions_per_user_df)
print(df)