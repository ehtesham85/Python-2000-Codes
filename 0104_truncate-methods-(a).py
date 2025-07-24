with open("myyfile.txt", "w") as f:
    
    f.write("Hello Sir\n")
    f.truncate(5)             # ho many bytes will store in file 

with open("myyfile.txt", "r") as f:
    print(f.read())


  