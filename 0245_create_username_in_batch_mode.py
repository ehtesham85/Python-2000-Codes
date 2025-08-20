# Create a file of username in batch mode

infileName = input("What file are the name in ?")
outfileName = input("What file should the username go in ?")

infile = open("infileName", "r")
outfile = open("outfileName", "w")

first, last = line.split()

uname = (first[0] + last[:7]).lower()
print(uname, file=outfile)

infile.close()
outfile.close()

print("Usernames have been written to", outfileName)
