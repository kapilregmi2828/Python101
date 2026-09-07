arr = [10, 12, 13, 15, 14, 9, 7, 97]

smallest = arr[0]
largest = arr[0]

for num in arr:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

x = smallest,largest

print(x)




