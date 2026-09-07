def min_max(arr):
    smallest = arr[0]
    largest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest,largest

x = [10, 12, 5, 7, 9, 2, 4]

print(min_max(x))

(a, b) = min_max(x)

print("Difference between max and min is:", (b-a))