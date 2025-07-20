import time
t=time.strftime('%H,%M,%S')
# n=int(time.strftime('%H'))
# print(n)
n=int(input("Enter the hour : "))
if (n>=0 and n<12):
    print("Good Morning Sir!")
elif (n>=12 and n<17):
    print("Good Afternoon Sir!")
elif (n>=17 or n<0):
    print("Good Night Sir!")
  