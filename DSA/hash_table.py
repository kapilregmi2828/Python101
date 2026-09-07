my_List = [
    [], [], [], [], [], [], [], [] ,[], []
    ]

def hash_function(name):
    sum_of_chars = 0
    for char in name:
        sum_of_chars += ord(char)

    return sum_of_chars % 10

def add(name):
    index = hash_function(name)
    my_List[index].append(name)

def contains(name):
    index = hash_function(name)
    return name in my_List[index] 
add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
add('Stuart')
print(my_List)

print("The list contains:", contains('Pete'))
print("The list contains:", contains('Kapil'))

