# #          Lists in Python
# marks=[3, 5, 6, "Ehtesham", True, 6, 7, 2, 32, 345, 23]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])                    #Through Error because index is out of range
# print(marks[len(marks)-3])         #Negative Index
# print(marks[5-3])                  #Positive Index
# print(marks[2])                    #Positive Index  

# if 7 in marks:
#     print("Yes")
# else:
#     print("No")

# # Same thing applies for strings as well!
# if "tes" in "Ehtesham":
#     print("Yes")
# else:
#     print("No")


# #           Slicing (Jump Index)
# print(marks)
# print(marks[1:9])
# print(marks[1:9:3])


#           List Comprehensions
lst=[ i*2 for i in range(10)]
print(lst)
lst=[ i*2 for i in range(10) if i%2==0]
print(lst)