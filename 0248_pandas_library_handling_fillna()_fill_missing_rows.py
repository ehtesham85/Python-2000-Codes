# fillna
# fill missing values

import pandas as pd

data = {
  "Name":["Ali","None", "Ahmet","Mehmet","Hasan"],
  "Age":[23,None,25,26,27],
  "Salary":[1000,None,3000,4000,5000]
}

df = pd.DataFrame(data)
print("Before Remove Missing Values")
print(df)


df["Age"].fillna(df["Age"].mean(), inplace=True)
# df["Name"].fillna("No Name", inplace=True)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)
print("After Remove Missing Values")
print(df)

