import pandas as pd

data = {
    "Name" : ["A", "B", "C", "D", "E", "F", "G"],
    "Age": [28, 40, 25, 32, 45, 30, 22],
    "Salary" : [50000, 55000, 45000, 65000, 70000, 52000, 29000],
    "PerformanceScore" : [85, 78, 92, 88, 95, 80, 75]
}

df = pd.DataFrame(data)
print("Before Sorting : ")
print(df)

df.sort_values(by="Age", ascending=False , inplace=True)
print("After Sorting : ")
print(df)
