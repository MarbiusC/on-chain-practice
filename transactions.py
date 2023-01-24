# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data into a pandas dataframe
df = pd.read_csv("transactions.csv")

# Print the first 5 rows of the data
print(df.head())

# Find the total number of transactions for each user
user_transactions = df.groupby("user_id").size().reset_index(name="total_transactions")
print(user_transactions)

# Find the average transaction value for each user
user_avg_value = df.groupby("user_id")["amount"].mean().reset_index(name="avg_transaction_value")
print(user_avg_value)

# Find the top 10 users with the highest total transaction value
top_users = df.groupby("user_id")["amount"].sum().nlargest(10).reset_index(name="total_transaction_value")
print(top_users)

# Create a histogram of transaction values
plt.hist(df["amount"], bins=50)
plt.xlabel("Transaction Amount")
plt.ylabel("Frequency")
plt.title("Transaction Amount Histogram")
plt.show()
