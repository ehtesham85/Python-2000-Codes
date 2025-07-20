            # print list simply
fruits = ["Apple","Banana","Cherry"]   # Assign Elements to list
print(fruits)                          # Print Full list
print(fruits[0])                       # Print first element
fruits[0] = "kiwi"                     # change first list
print(fruits[0])                       #print first element
print(fruits[1])                       #print second element
print(fruits[2])                       #print third element


            # print fruits by loop
for fruit in fruits:
 print("I like to eat", fruit)


            # logic building using if-else
marks=[75,45,40,50,71,64]
for score in marks:
  if score>=50:
    print(score," pass")
  else:
    print(score," fail")
