import pandas as pd

data = {
    "Name" : ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Age": [28, None, 40, 25, 32, 45, 30, 22],
    "Salary" : [50000, None, 55000, 45000, 65000, 70000, 52000, 29000],
    "PerformanceScore" : [85, None, 78, 92, 88, 95, 80, 75]
}

df = pd.DataFrame(data)
print("Before Interpolation : ")
print(df)

df.interpolate(method="linear", axis=0, inplace=True)
print("After Interpolation : ")
print(df)
