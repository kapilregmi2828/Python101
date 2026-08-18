# span() returns a tuple containing the start and end positions of the match.

# string returns the string passed into the function

# group() returns the part of the string where there was a match

import re

txt = "The rain in Spain"

x = re.search(r"\bS\w+",txt) 
# r specifies raw string tell to ignore \ 
# \b returns the match where specified character is at the begaining or end of the word
# S searches capital S in the string provided 
#\w+ find words

print(x.span()) # returns the position start and end (Tuple)

print(x.string) # prints the string 

print(x.group()) # prints the word where there was a match. 


