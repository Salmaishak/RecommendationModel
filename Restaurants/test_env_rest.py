#loop for 1000 choosing amentities
from Restaurants.create_test_users_rest import *

df=[]
for x in range(1,31):
    df=user_profile_rest(x)
    print(x)
    intoCSV(df)