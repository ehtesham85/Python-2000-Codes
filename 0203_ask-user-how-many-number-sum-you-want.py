# ask user how many numbers you want to sum

sum = 0
n = int(input("How many numbers are to be summed : "))
for i in range(n):
      sum += int(input("Enter a number : "))

print("Sum of the numbers is : ", sum)
