import pandas as pd

df_customers = pd.DataFrame({
  "CustomerID": [1,2,3],
  "Name": ["Ali","Musa","Ibnam"]
})

df_orders = pd.DataFrame({
  "CustomerID": [1,2,4],
  "OrderAmount": [250, 450, 300]
})


df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="inner")
print("Inner join : ")
print(df_merged)
