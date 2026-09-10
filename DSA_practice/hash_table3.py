my_list = [
    [],[],[],[],[],[],[],[],[],[]
]

def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars = ord(char)
    return sum_of_chars % 10

def add(name):
    index = hash_function(name)
    my_list[index].append(name)

def contain(name):
    index = hash_function(name)
    return name in my_list[index]

add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
add('Stuart')
print(my_list)

print("Index of name:", hash_function('Stuart'))

print("Bob is in the list.", contain('Bob'))
print("Kapil is in the list.", contain('Kapil'))
