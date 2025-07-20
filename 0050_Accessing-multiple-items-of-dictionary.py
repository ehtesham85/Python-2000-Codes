info={'name':'Ehtesham','age':21,'eligible':True}
# print(info.keys())
# print(info.values())

# for key in info.keys():
#    print(info[key])
#    print(f"The value corrsponfing to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
     print(f"The value corresponding to the key {key} is {value}")


