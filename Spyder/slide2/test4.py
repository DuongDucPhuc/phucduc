# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:15:21 2024

@author: ADMIN
"""

import pandas as pd
import numpy as np

# Dữ liệu lỗi
errors_one = pd.Series([5, 10, 5, 10, 5, 10, 5, 10, 5, 10])
errors_two = pd.Series([5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 1000])

# Tính MAE và RMSE cho errors_one
mae_one = errors_one.mean()  # Hoặc errors_one.sum()/len(errors_one)
rmse_one = np.sqrt((errors_one**2).mean())  # Hoặc np.sqrt((errors_one**2).sum()/len(errors_one))

# Hiển thị kết quả cho errors_one
print(f"MAE for errors_one: {mae_one}")
print(f"RMSE for errors_one: {rmse_one}")

# Tính MAE và RMSE cho errors_two
mae_two = errors_two.mean()  # Hoặc errors_two.sum()/len(errors_two)
rmse_two = np.sqrt((errors_two**2).mean())  # Hoặc np.sqrt((errors_two**2).sum()/len(errors_two))

# Hiển thị kết quả cho errors_two
print(f"MAE for errors_two: {mae_two}")
print(f"RMSE for errors_two: {rmse_two}")