 # Q.6.4

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
sales="company_sales_data.csv"
data = pd.read_csv(sales)

plt.figure(figsize=(10, 6))
sns.lineplot(x="month_number", y="total_profit", data=data, marker="o", color="b")
plt.title("Total Profit Over All Months")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 8))
for product in data.columns[1:7]:  
    sns.lineplot(x="month_number", y=product, data=data, label=product, marker="o")

plt.title("Sales Data of All Products Over Months")
plt.xlabel("Month Number")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()

data_sum = data.drop("month_number", axis=1).sum() 
plt.figure(figsize=(12, 8))
sns.barplot(x=data_sum.index, y=data_sum.values, palette="Set2")
plt.title("Total Sales and Profit for All Attributes")
plt.xlabel("Attributes")
plt.ylabel("Total Value")
plt.xticks(rotation=30)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
