arr = [7,11,12,8,4,9,14]
min_value = arr[0]
for i in arr:
    if i<min_value:
        min_value = i
print("Minimum value in the array is:", min_value)

print(min(arr))
