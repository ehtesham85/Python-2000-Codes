# If the annual investment is $100, the annual return is 3%, and the number of years is 10, the total amount of money will be $133.89.

print("This Program calculates the future value of a 10-year investment.")

principal=eval(input("Enter the initial principal : "))
apr = eval(input("Enter the annual interest rate : "))

for i in range(10):
   principal=principal*(1+apr)
  
print("the value in 10 Years ia : ",principal)