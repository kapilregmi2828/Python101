import re

txt = "The rain in Spain"

x = re.findall("ai",txt)
print(x) # ['ai', 'ai']

y = re.findall("Nepal",txt)
print(y) # []

a = re.search("\s",txt)
print("The first white-space character is located in position:", a.start())
# The first white-space character is located in position: 3

b = re.search("Nepal",txt)
print(b)
# None