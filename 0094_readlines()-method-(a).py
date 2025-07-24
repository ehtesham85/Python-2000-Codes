# readline() method
f=open('myyfile.txt','r')
while True:
   line=f.readline()
   if not line:
      break
   print(line)