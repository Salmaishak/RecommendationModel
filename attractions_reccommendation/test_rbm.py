from rbm import *
import pandas as pd

attractions_data = pd.read_csv('attractions.csv')
ratings_data = pd.read_csv('user_profiling3010.csv')  # all ratings 5

df =rbm(attractions_data, ratings_data, 'cairo', 20)
# print(type(df))
# df=df['attraction_id']
# print(len(df))
print(df)
timesAttract= pd.read_csv('Attractions open hours.csv')
select= timesAttract.loc[:, ['attraction_id','open_time','close_time']]
print(select)
joinedTimes = timesAttract.join(df.add_suffix('_ratings'), on='attraction_id', how='inner')
print(joinedTimes)