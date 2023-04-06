def profiling_new_user(user_id, attraction_id, rating, city):
    with open("user_profiling3010.csv", 'a') as file:
        file.write("\n")
        file.write(user_id)
        file.write(",")
        file.write(attraction_id)
        file.write(",")
        file.write(rating)
        file.write(",")
        file.write('F')
        file.write(",")
        file.write(city)

# profiling_new_user('31','205','4','cairo')