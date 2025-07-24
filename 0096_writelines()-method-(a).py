# writeline() method
f=open('myyfile.txt','w')
line=[ 'Assalam-o-Alaikum\n','How are you?\n','I am fine\n','Thank you\n','Regards\n', 'Ehtesham\n']
f.writelines(line)
f.close()
