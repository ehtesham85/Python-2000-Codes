import enum


marks=[12, 56, 32, 98, 12, 45, 1, 4]

index=0
for mark in marks:
    print("Marks are:", mark)
    if(index==3):
        print("Ehtesham, awesome!")
    index+=1


for index, mark in enumerate(marks,start=1):
      print(mark)
      if(index==3):
          print("Ehtesham, awesome!")


colors=["Red", "Green", "Blue", "Yellow"]
for index, col in enumerate(colors):
      print(index, col)

