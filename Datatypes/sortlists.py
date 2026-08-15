fruits = ["Mango", "Apple", "Orange", "Kiwis", "Banana", "Apricot"]
print(fruits)
fruits.sort()
print(fruits)

# complex example of sorting list close to 50
def fun1(n):
    return abs(n-50)


numlist = [100, 50, 62, 23, 82]
numlist.sort(key = fun1)

print(numlist)

