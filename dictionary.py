# Dictionary can be nested. 
# Loop through dictionary

x = {"type": "vehicle", "brand": "Honda"}

for a, b in x.items():
    print(a, b)

for c in x.keys():
    print(c)

for d in x.values():
    print(d)

# copying the dictionary can be done by using copy() method and dict() function. Lets see!

d1 = {"fruit": "apple", "color": "red", "taste": "sweet"}

'''d2 = d1.copy()

print(d1)
print(d2)
'''
d2 = dict(d1)
print(d2)