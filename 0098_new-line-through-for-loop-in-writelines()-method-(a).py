# writeline() method
f=open('myyfile.txt','w')
lines=[ 'Hello','How are you?','I hope you are fine. I will see you soon man.','Thank you','Regard', 'Ehtesham']
for line in lines:
  f.writelines(line + '\n')
f.close()
