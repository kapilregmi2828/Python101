# split() function returns a list where the string has been split at each match.

import re
txt = "The rain in Spain"

x = re.split("\s",txt)
print(x) # ['The', 'rain', 'in', 'Spain']

y = re.split("\s", txt, 1) # splits at the first occurence only
print(y) #['The', 'rain in Spain']


