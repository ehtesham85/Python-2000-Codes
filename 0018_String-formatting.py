  letter = "Hey my name is {1} and I'm from {0}"
  country="Pakistan"
  Name="Ehtesham"
  print(letter.format(country,Name))     #old method

  print(f"Hey my name is {Name} and I'm from {country}")   #new method

  price=49.090000
  txt=f"For only {price:.2f} dollars"
  print(txt)
  # print(txt.format())