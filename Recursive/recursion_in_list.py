def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])

list1 = list(map(int,input("Enter your list: ").split()))

print(sum_list(list1))

