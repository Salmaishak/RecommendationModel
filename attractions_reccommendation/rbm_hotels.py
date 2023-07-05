import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# %matplotlib inline

def rbm(hotels_data, ratings_data, city, userid):
    hotels_data['List Index'] = hotels_data.index

    # merging attraction_df with ratings_df by attraction_id
    merged_data = hotels_data.merge(ratings_data, on='hotelID')
    merged_data = merged_data.drop(
        ['name', 'ratings', 'prices', 'amenities', 'location', 'description', 'City', 'Latitude', 'Longitude',
         '''"Latitude,Longitude"''', 'Price Range', 'empty amenities',
         ], axis=1)

    # group by user_id
    user_group = merged_data.groupby('user_id')

    # number of users used for training
    no_of_training_users = 20
    # Creating the training list
    train_X = []
    # For each user in the group
    for userID, curUser in user_group:
        # Create a temp that stores every hotel's rating
        temp = [0] * len(hotels_data)
        # For each hotel in curUser's hotel list
        for num, hotel in curUser.iterrows():
            # Divide the rating by 5 and store it
            temp[hotel['List Index']] = hotel['rating'] / 5.0

        train_X.append(temp)

        if no_of_training_users == 0:
            break
        no_of_training_users -= 1

    # -----------------  Model's Parameters  -----------------
    import tensorflow.compat.v1 as tf

    hidden_units = 1  # can be set to any number
    visible_units = len(hotels_data)
    tf.disable_v2_behavior()
    vb = tf.placeholder("float", [visible_units])  # no. of unique attractions
    hb = tf.placeholder("float", [hidden_units])  # no. of features
    W = tf.placeholder("float", [visible_units, hidden_units])  # weight matrix

    # Phase 1: Input Processing
    v0 = tf.placeholder("float", [None, visible_units])
    _h0 = tf.nn.sigmoid(tf.matmul(v0, W) + hb)
    h0 = tf.nn.relu(tf.sign(_h0 - tf.random_uniform(tf.shape(_h0))))

    # Phase 2: Reconstruction
    _v1 = tf.nn.sigmoid(tf.matmul(h0, tf.transpose(W)) + vb)
    v1 = tf.nn.relu(tf.sign(_v1 - tf.random_uniform(tf.shape(_v1))))
    h1 = tf.nn.sigmoid(tf.matmul(v1, W) + hb)

    # Learning rate
    alpha = 1.0
    # Create the gradients
    w_pos_grad = tf.matmul(tf.transpose(v0), h0)
    w_neg_grad = tf.matmul(tf.transpose(v1), h1)

    # Calculate the Contrastive Divergence to maximize
    CD = (w_pos_grad - w_neg_grad) / tf.to_float(tf.shape(v0)[0])

    # Create methods to update the weights and biases
    update_w = W + alpha * CD
    update_vb = vb + alpha * tf.reduce_mean(v0 - v1, 0)
    update_hb = hb + alpha * tf.reduce_mean(h0 - h1, 0)

    # Mean Absolute Error Function
    err = v0 - v1
    err_sum = tf.reduce_mean(err * err)

    # RMSE
    rmse = tf.sqrt(err_sum)

    # initialize variables with zeros
    # Current weight
    cur_w = np.zeros([visible_units, hidden_units], np.float32)
    # Current visible unit biases
    cur_vb = np.zeros([visible_units], np.float32)
    # Current hidden unit biases
    cur_hb = np.zeros([hidden_units], np.float32)
    # Previous weight
    prv_w = np.zeros([visible_units, hidden_units], np.float32)
    # Previous visible unit biases
    prv_vb = np.zeros([visible_units], np.float32)
    # Previous hidden unit biases
    prv_hb = np.zeros([hidden_units], np.float32)
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    epochs = 15
    batchsize = 10
    errors = []
    # mean absolute error------------------------------
    for i in range(epochs):
        for start, end in zip(range(0, len(train_X), batchsize), range(batchsize, len(train_X), batchsize)):
            batch = train_X[start:end]
            cur_w = sess.run(update_w, feed_dict={v0: batch, W: prv_w, vb: prv_vb, hb: prv_hb})
            cur_vb = sess.run(update_vb, feed_dict={v0: batch, W: prv_w, vb: prv_vb, hb: prv_hb})
            cur_nb = sess.run(update_hb, feed_dict={v0: batch, W: prv_w, vb: prv_vb, hb: prv_hb})
            prv_w = cur_w
            prv_vb = cur_vb
            prv_hb = cur_nb
        errors.append(sess.run(err_sum, feed_dict={v0: train_X, W: cur_w, vb: cur_vb, hb: cur_nb}))
        print("mae: ", errors[-1])

    # root mean square error------------------------------
    for i in range(epochs):
        for start, end in zip(range(0, len(train_X), batchsize), range(batchsize, len(train_X), batchsize)):
            batch = train_X[start:end]
            cur_w = sess.run(update_w, feed_dict={v0: batch, W: prv_w, vb: prv_vb, hb: prv_hb})
            cur_vb = sess.run(update_vb, feed_dict={v0: batch, W: prv_w, vb: prv_vb, hb: prv_hb})
            cur_nb = sess.run(update_hb, feed_dict={v0: batch, W: prv_w, vb: prv_vb, hb: prv_hb})
            prv_w = cur_w
            prv_vb = cur_vb
            prv_hb = cur_nb
        errors.append(sess.run(rmse, feed_dict={v0: train_X, W: cur_w, vb: cur_vb, hb: cur_nb}))
        print("rmse: ", errors[-1])
    # -----------------  Recommendation  -----------------
    # Selecting the input user
    inputUser = [train_X[userid]]
    # Feeding in the user and reconstructing the input
    hh0 = tf.nn.sigmoid(tf.matmul(v0, W) + hb)
    vv1 = tf.nn.sigmoid(tf.matmul(hh0, tf.transpose(W)) + vb)
    feed = sess.run(hh0, feed_dict={v0: inputUser, W: prv_w, hb: prv_hb})
    rec = sess.run(vv1, feed_dict={hh0: feed, W: prv_w, vb: prv_vb})

    scored_attractions_df_15 = hotels_data
    scored_attractions_df_15["Recommendation Score"] = rec[0]

    # all attr that the user has seen before
    attractions_data_15 = merged_data[merged_data['user_id'] == userid]

    merged_data_15 = scored_attractions_df_15.merge(attractions_data_15, on='hotelID', how='outer')
    # merged_data_15 = merged_data_15.drop('List Index_y', axis=1).drop('user_id', axis=1)

    # first 20 hotel
    # print(merged_data_15.sort_values(["Recommendation Score"], ascending=False).head(20))

    # filtering by city and by NaN ratings (which are the attractions the user hasn't seen)
    attractions_15_df = pd.DataFrame(merged_data_15,
                                     columns=['hotelID', 'name', 'ratings', 'prices', 'amenities',
                                              'location',
                                              'description', 'City', 'Latitude', 'Longitude', 'Price Range',
                                              'List Index_x',
                                              'Recommendation Score', 'rating'])

    # print("------------------- first 20 attractions for user {} -------------------".format(userid))
    attractions_15_df = (
        attractions_15_df.loc[(merged_data_15['city'] == city) & (merged_data_15['rating'].isna())].sort_values(
            ["Recommendation Score"], ascending=False).head(20))
    return attractions_15_df

hotels_data = pd.read_csv('../Hotels/Allhotels.csv')
ratings_data = pd.read_csv('../Hotels/user_profiling.csv')  # all ratings 5

df = rbm(hotels_data, ratings_data, 'cairo', 20)