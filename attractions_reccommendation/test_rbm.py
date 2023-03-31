from rbm import *
import pandas as pd

attractions_data = pd.read_csv('attractions.csv')
ratings_data = pd.read_csv('user_profiling3010.csv')  # all ratings 5

rbm(attractions_data, ratings_data, 'luxor', 20)

