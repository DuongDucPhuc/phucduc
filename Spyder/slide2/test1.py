# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:12:30 2024

@author: ADMIN
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Đọc tập dữ liệu dc_airbnb.csv và làm sạch dữ liệu
dc_listings = pd.read_csv('E:/Spyder/dc_airbnb.csv')

# Loại bỏ dấu phẩy và ký hiệu đô la khỏi cột price, sau đó chuyển thành kiểu float
dc_listings['price'] = dc_listings['price'].str.replace(',', '').str.replace('$', '').astype(float)

# Chia dữ liệu thành training set (75%) và test set (25%)
train_df, test_df = train_test_split(dc_listings, test_size=0.25, random_state=42)

# Hàm predict_price sử dụng train_df để đoán bộ dc_listings
def predict_price(new_listing):
    temp_df = train_df.copy()  # Chỉ sử dụng dữ liệu training
    # Tính khoảng cách giữa số lượng khách và các không gian khác trong tập training
    temp_df['distance'] = temp_df['accommodates'].apply(lambda x: abs(x - new_listing))
    
    # Sắp xếp và chọn 5 hàng đầu tiên
    nearest_neighbors = temp_df.sort_values('distance').head(5)
    predicted_price = nearest_neighbors['price'].mean()

    return predicted_price

# Sử dụng phương thức apply để dự đoán giá cho tất cả các hàng trong test_df
test_df['predicted_price'] = test_df['accommodates'].apply(predict_price)

# Hiển thị 5 hàng đầu tiên trong tập test để trực tiếp vê giá trị dự đoán
print(test_df[['accommodates', 'price', 'predicted_price']].head())