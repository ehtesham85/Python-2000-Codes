# Convert a sequence of unicode numbers into a string of text
inString = input("Enter a unicode-encoded message : ")
message=""
for numStr in inString.split():
    codeNum=int(numStr)
    message=message+chr(codeNum)
print("The decode message is : ",message)

