# continue
for i in range(12):
  if(i==10):
    print("Skip the Iteration")
    continue
  print("5 x",i+1,"=",5*(i+1))


# break
i=0
while True:
  print(i)
  i=i+1
  if(i%100==0):
    break