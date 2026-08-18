# this is exception handling method. It will catch any runtime error and try to bypass it. 

try:
    age = int(input("How old are you?"))
except:
    print("Please enter a number!")
finally:
    print("You are",age, "years old." )

