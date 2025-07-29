import os

files=os.listdir("clutteredFolder")
i=0
for file in files:
  if file.endswith(".py"):
     print(file)
     os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{i}.py")
     i=i+1



