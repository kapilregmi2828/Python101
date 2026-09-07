
def find_min_max(arr):
    smallest = arr[0]
    largest = arr[0]

    for num in arr:
        if num < smallest:
            smallest = num

        if num > largest:
            largest = num
    return smallest, largest


a = [10,5,20,8,15]
print(find_min_max(a))

(x,y) = find_min_max(a)

print(y-x)