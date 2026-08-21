import os

if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
    print("The file has been deleted.")

else:
    print("The file doesn't exist. ")