# 3 
import numpy as np

X = 75 + 75  # ASCII sum for initials "K K"
sales = np.array([X, X+50, X+100, X+150, X+200])  

tax_rate = ((X % 5) + 5) / 100 
tax_amount = sales * tax_rate

discount_rates = np.where(sales < (X+100), 0.05, 0.10)
discounted_sales = sales * (1 - discount_rates)

weekly_sales = np.vstack([sales] * 3) 
week_factors = np.array([1.00, 1.02, 1.04]).reshape(3, 1)  
adjusted_sales = weekly_sales * week_factors 

print("Sales Dataset:", sales)
print("Tax Amount on Each Sale:", tax_amount)
print("Discounted Sales:", discounted_sales)
print("Weekly Sales Data:\n", weekly_sales)
print("Adjusted Sales with Weekly Increase:\n", adjusted_sales)
