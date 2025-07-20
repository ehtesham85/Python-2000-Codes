questions=["What is the capital of Pakistan?","What is 10+20?","What is the color of Mango?","Which Animal says meow?"]

options=[["A.Islamabad","B.Karachi","C.Lahore","D.Peshawar"],["A.30","B.20","C.10","D.40"],["A.Red","B.Yellow","C.Green","D.Blue"],["A.Dog","B.Cat","C.Cow","D.Horse"]]

answers=["A","A","B","B"]

prizes=[1000,2000,3000,4000]


user_answer=["A","B","B","B"]

total=0

print("\t\tWelcome to KBC")

for i in range(len(questions)):
     print(f"Q{i+1}: questions{i+1}")
     for option in options[i]:
         print(option)

user_ans=user_answer[i]
print(f"User Selected: {user_ans}")

if user_ans==answers[i]:
    total+=prizes[i]
    print(f"Correct Answer! You have won {prizes[i]}")
else:
    print("Wrong Answer! You have lost the game")

print(f"You take home {total}")


