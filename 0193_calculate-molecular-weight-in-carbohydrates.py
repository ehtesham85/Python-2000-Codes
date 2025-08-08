# Compute molecular weight of carbohydrates in (grams per mole) of given carbohydrates

c = int(input("Enter the number of carbon atoms : "))
h = int(input("Enter the number of hydrogen atoms : "))
o = int(input("Enter the number of oxygen atoms : "))

gpm = c*(12.0107) + h*(1.0079) + o*(15.9994)

print("Molecular weight of carbohydrate in (grams per mole ) is : ", gpm)
