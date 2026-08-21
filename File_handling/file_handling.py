f = open("demofile.txt") # opening the file 
print(f.read()) # reading the file 


# with open("demofile.txt") as f: # opening the file with 'with' statement. 
#     print(f.read())

with open("demofile.txt") as f:
    #print(f.readlines())
    #print(f.readline())
    print(f.read(5))

with open("demofile.txt") as f:
    for x in f:
        print(x)

f.close()