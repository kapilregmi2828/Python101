# max in the list using recursive function

def max_of_list(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        max_of_rest = max_of_list(numbers[1:])

    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

x = list(map(int, input("Enter your list with space in between: ").split()))
print(max_of_list(x))