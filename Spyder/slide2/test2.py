# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:13:56 2024

@author: ADMIN
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Đọc tập dữ liệu dc_airbnb.csv và làm sạch dữ liệu
dc_listings = pd.read_csv('E:/Spyder/dc_airbnb.csv')
dc_listings['price'] = dc_listings['price'].str.replace(',', '').str.replace('$', '').astype(float)

# Chia dữ liệu thành training set (75%) và test set (25%)
train_df, test_df = train_test_split(dc_listings, test_size=0.25, random_state=42)

# Sửa đổi hàm predict_price để sử dụng cột bathrooms thay vì accommodates
def predict_price(new_listing):
    temp_df = train_df.copy()  # Chỉ sử dụng dữ liệu training
    # Tính khoảng cách giữa số lượng bathrooms và các không gian khác trong tập training
    temp_df['distance'] = temp_df['bathrooms'].apply(lambda x: abs(x - new_listing))
    
    # Sắp xếp và chọn 5 hàng đầu tiên
    nearest_neighbors = temp_df.sort_values('distance').head(5)
    # Tính giá trung bình của 5 không gian gần nhất
    predicted_price = nearest_neighbors['price'].mean()

    return predicted_price

# Sử dụng phương thức apply để dự đoán giá cho tất cả các hàng trong test_df
test_df['predicted_price'] = test_df['bathrooms'].apply(predict_price)

# Tính squared error giữa giá thực tế và giá predicted
test_df['squared_error'] = (test_df['price'] - test_df['predicted_price']) ** 2

# Tính Mean Squared Error (MSE)
mse = test_df['squared_error'].mean()

# Hiển thị giá trị MSE
print(f"Mean Squared Error (MSE): {mse}")