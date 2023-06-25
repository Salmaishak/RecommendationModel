from rbm import *
import pandas as pd

attractions_data = pd.read_csv('attractions.csv')
ratings_data = pd.read_csv('user_profiling3010.csv')  # all ratings 5

df =rbm(attractions_data, ratings_data, 'cairo', 20)
# print(type(df))
# df=df['attraction_id']
# print(len(df))
print(df['city'])
timesAttract= pd.read_csv('Attractions open hours.csv')



joinedTimes = df.merge(timesAttract[['attraction_id', 'open_time', 'close_time', 'attraction_name', 'Latitude', 'Longitude', 'city']], on='attraction_id', how='inner')

print(joinedTimes)

# select= timesAttract.loc[:, ['attraction_id','open_time','close_time','city']]
# print(select['city'])
# joinedTimes = timesAttract.join(df.add_suffix('_ratings'), on='attraction_id', how='inner')
# print(joinedTimes['city'])
# filtered_joined_times = joinedTimes.loc[joinedTimes['city'] == 'giza']
# print(filtered_joined_times['city'])