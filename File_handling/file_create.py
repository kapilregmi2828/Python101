f = open("newfile.txt", "x")
f.write("We have created a new file.")

with open("newfile.txt") as f:
    print(f.read())