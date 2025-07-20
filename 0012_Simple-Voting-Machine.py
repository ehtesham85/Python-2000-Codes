print("\tVoter Eligibility Criteria\n")
age = int(input("Enter your age : "))
if (age >= 18):
  print("You are eligible to vote")
  print("You can vote for your favourite candidate")
else:
  print("You are not eligible because you are younger than 18")
  print("You can vote after 18")
