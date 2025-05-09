import requests
import pandas as pd
import matplotlib.pyplot as plt

# Load data
ticker = "F"
url = f"https://raw.githubusercontent.com/itb-ie/midterm_data/refs/heads/main/{ticker}.csv"
with open("company.csv", "w") as f:
    f.write(requests.get(url).text)
df = pd.read_csv("company.csv", index_col="Date")


#1 How many rows does the dataframe have?
print("Number of rows:")
print(len(df))

#2 What are the column names?
print("\nColumn names:")
print(df.columns)

#3 What was the opening stock value on April 9th? We first need to make sure the index is parsed as dates
df.index = pd.to_datetime(df.index)
print("\nOpening value on April 9th:")
print(df.loc["2025-04-09", "Open"])

#4 Plot one column
plt.plot(df.index, df["Close"])
plt.title("Ford Stock Close Price")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.grid(True)
plt.show()
