# this is a function for finding maximum value

def function1(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for x in numbers:
        if x > max_num:
            max_num = x
    return max_num

print(function1(1,5,10,11,100,156,2,8))
print(function1())


