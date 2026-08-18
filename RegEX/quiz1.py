import re

txt = "The rain in Spain"

x = re.findall('[a-j]', txt)

print(x)

y = re.search("a", txt)
print(y.start())