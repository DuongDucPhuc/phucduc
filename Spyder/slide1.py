# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:00:08 2024

@author: ADMIN
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
dc_listings = pd.read_csv('E:/Spyder/dc_airbnb.csv')
print(dc_listings.head(1))
first_accommodates = dc_listings.iloc[0]['accommodates']
our_accommodates = 3
first_distance = abs(first_accommodates-our_accommodates)
print(first_distance)
dc_listings['distance'] = dc_listings['accommodates'].apply(lambda x: abs(x-3))
dc_listings['distance'].value_counts()
print(dc_listings['distance'])
print(dc_listings[dc_listings["distance"] == 0] ["accommodates"])
shuffled_index = np.random.permutation(dc_listings.index)
dc_listings = dc_listings.loc[shuffled_index]
dc_listings = dc_listings.sort_values('distance')
print(dc_listings['price'].head(10))
stripped_commas = dc_listings['price'].str.replace(',',"")
stripped_dollar_signs = stripped_commas.str.replace('$',"") 
dc_listings['price'] = stripped_dollar_signs.astype(float)
mean_price = dc_listings['price'].head(5).mean()
print(mean_price)
def predict_price(new_listing):
    temp_df = dc_listings.copy
    temp_df['distance'] = temp_df['accommodates'].apply(lambda x: abs (x-new_listing))
    nearest_neighbors = temp_df.sort_values('distance').head(5)
    predicted_price = nearest_neighbors['price'].mean()
    return predicted_price
acc_one = predict_price(1)
acc_two = predict_price(2)
acc_four = predict_price(4)
print(f"Suggested price for 1 person: {acc_one}")
print(f"Suggested price for 2 people: {acc_two}")
print(f"Suggested ngôn ngữ for 4 people: {acc_four}")


