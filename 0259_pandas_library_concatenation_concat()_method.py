# Concatenation
'''
vertically (row-wise)
horizontally (colum-wise)

pd.concate([df1,df2], axis=0, ignore_index=True)

[df1,df2] = 
axis = 1
ignore_index = True
'''

import pandas as pd

df_region1 = pd.DataFrame({
  "CustomerID":[1,2],
  "Name":["Ali","Ibnam"]
})

df_region2 = pd.DataFrame({
  "CustomerID":[3,4],
  "Name":["Ahmad","Musa"]
})


df_concate = pd.concat([df_region1, df_region2], axis=0, ignore_index=True)

print("Concatenation of two dataframes : ")
print(df_concate
     
     
     )