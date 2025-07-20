#strings are immutable
a = "Ehtesham!! !!!!! Ehtesham"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Ehtesham", "Ali"))
print(a.split(" "))
print(a.count("Ehtesham"))
heading = "introduction to python"
print(heading.capitalize())
print(heading.center(50))

str1 = "Welcome to the console !!!"
print(str1.endswith("!!!"))
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
print(str1.index("is"))
print(str1.find("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())
str1 = "hello world"
print(str1.islower())
str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "        "
print(str1.isspace())
str2 = "       "
print(str2.isspace())
str1 = "World Health Organization"
print(str1.istitle())
str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language"
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())
