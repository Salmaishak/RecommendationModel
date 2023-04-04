#loop for 1000 choosing amentities
from rest_user_profiling_test import *

df=[]
for x in range(1,31):
    df=user_profile_rest(x)
    print("Dataframe: ")
    print(df)
    # print(x)
    intoCSV(df)