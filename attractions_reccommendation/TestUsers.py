# loop for 1000 choosing amentities
from user_profiling_code import *

# arrayOfCities = ['Sharm El Sheikh', 'Cairo', 'Luxor', 'Giza', 'Al-Fayyum']
df = []
for x in range(1, 134):
    df = user_profile(x)
    print(x)
    intoCSV(df)
