# fillna
# fill missing values

import pandas as pd

data = {
  "Name":["Ali","None", "Ahmet","Mehmet","Hasan"],
  "Age":[23,None,25,26,27],
  "City":["Istanbul","None","Ankara","Izmir","Bursa"]
}

df = pd.DataFrame(data)
print("Before Remove Missing Values")
print(df)

print("After Remove Missing Values")
df.fillna(0, inplace=True)
print(df)

