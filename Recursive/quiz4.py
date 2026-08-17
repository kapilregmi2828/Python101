# recursive function to calculate the sum of list. 

def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])

x = list(map(int, input("Enter your list using space in between: ").split()))
print(sum_list(x))