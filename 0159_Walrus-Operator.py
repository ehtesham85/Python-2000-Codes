# Walrus operator


# a=True
# print(a:=False)


# numbers = [1, 2, 3, 4, 5]
# while(n:= len(numbers))>0:
#    print(numbers.pop())

# print(numbers)


# simple method
# foods=list()
# while True:
#     food=input("Enter your food name:")
#     if food=="quit":
#         break
#     foods.append(food)

# With Walrus Operator
foods=list()
while (food:=input("Enter your food name:")) != "quit":
    foods.append(food)

