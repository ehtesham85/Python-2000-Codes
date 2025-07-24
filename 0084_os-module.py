import os

if(os.path.exists("data")):
os.mkdir("data")

for i in range(1, 50):
    os.mkdir(f"data/day{i+1}")