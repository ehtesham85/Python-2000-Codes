# applePrice = 190
# budget = 200
# if (applePrice<=budget):
#     print("You can buy an apple")
#     print("Have a nice day")
# else:
#     print("You cannot buy an apple")
#     print("Sorry")



# num=int(input("Enter the Value : "))
# if(num<0):
#     print("Negative Number")
# elif(num==0):
#     print("Zero")
# else:
#     print("Positive Number")


num=18
if(num<0):
    print("Negative Number")
elif(num>0):
    if(num<=10):
        print("Number is between 1-10")
    elif(num>10 and num<=20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")