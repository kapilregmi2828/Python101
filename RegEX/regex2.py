import re

txt = "The rain in Spain"

x = re.findall("ai",txt)
print(x)

y = re.findall("Nepal",txt)
print(y)

a = re.search("\s",txt)
print("The first white-space character is located in position:", a.start())

b = re.search("Nepal",txt)
print(b)