arr = [10,5,7,8,9,11,4]
min_value = arr[0]
for i in arr:
    if i<min_value:
        min_value = i
print("Minimum value in the array is:", min_value)

print(min(arr))