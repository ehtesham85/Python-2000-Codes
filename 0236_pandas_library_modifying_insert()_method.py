import pandas as pd

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda','Ehtesham','ALi','Ahmad'],
    'Age': [28, 24, 35, 32, 33, 34, 45],
    'City': ['New York', 'Paris', 'Berlin', 'London',"Karachi","Lahore","Islamabad"],
    'Salary': [70000, 80000, 50000, 60000, 50000, 60000,45000]
}
df=pd.DataFrame(data)
print(df)

# Add a new column 'Bonus' which is 10% of the salary
df["Bonus"] = df['Salary']*0.10
print(df)

