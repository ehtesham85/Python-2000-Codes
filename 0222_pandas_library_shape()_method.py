import pandas as pd

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Ali', 'Ahmad', 'Ehtesham', 'Gulshan'],
    'Age': [28, 24, 35, 32, 40, 45, 47, 39],
    'City': ['New York', 'Paris', 'Berlin', 'London', 'Islamabad', 'Karachi', 'Lahore', 'Peshawar']
}

df = pd.DataFrame(data)
print("Original DataFrame : ")
print(df)
print(f"Shape : {df.shape}")              # print rows and columns







