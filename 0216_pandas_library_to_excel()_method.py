import openpyxl
import pandas as pd

data = {
    "Name":["Ali","Ahmad","Ehtesham","Jutt","Gulshan","Gull"],
    "Age":[20,21,22,23,24,25],
    "City":["Islamabad","Karachi","Lahore","Peshawar","Quetta","Multan"]  
}

df = pd.DataFrame(data)
print(df)

df.to_excel("data.xlsx", sheet_name="Sheet1", index=False)

