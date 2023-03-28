#loop for 1000 choosing amentities
from Hotels.user_profile_Data.user_profiling_code import *
arrayOfCities=['Sharm El Sheikh','Cairo','Luxor','Giza','Al-Fayyum']
df=[]
for x in range(1,31):
    df=user_profile(x)
    print(x)
    intoCSV(df)