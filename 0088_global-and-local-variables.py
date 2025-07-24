x=4
print(4)

def hello():
    x=5
    print(f"The Local x is {x}"  )
    print("Hello Ehtesham")

print(f"The global x is {x}"  )
hello()
x=5
print(f"The global x is {x}"  )
