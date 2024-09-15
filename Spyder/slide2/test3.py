# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:14:36 2024

@author: ADMIN
"""

def predict_price(new_listing):
    temp_df = train_df.copy()  # Sao chép tập dữ liệu huấn luyện
    temp_df['distance'] = temp_df['bathrooms'].apply(lambda x: np.abs(x - new_listing))  # Tính khoảng cách dựa trên số phòng tắm
    temp_df = temp_df.sort_values('distance')  # Sắp xếp theo khoảng cách
    nearest_neighbors_prices = temp_df.iloc[0:5]['price']  # Lấy giá của 5 hàng xóm gần nhất
    predicted_price = nearest_neighbors_prices.mean()  # Tính giá dự đoán bằng trung bình của 5 hàng xóm gần nhất
    return predicted_price

# Áp dụng hàm dự đoán cho tập test
test_df['predicted_price'] = test_df['bathrooms'].apply(lambda x: predict_price(x))

# Tính squared error
test_df['squared_error'] = (test_df['predicted_price'] - test_df['price']) ** 2

# Tính Mean Squared Error (MSE)
mse = test_df['squared_error'].mean()

# Tính Root Mean Squared Error (RMSE)
rmse = mse ** (1/2)

# Hiển thị giá trị RMSE
print(rmse)