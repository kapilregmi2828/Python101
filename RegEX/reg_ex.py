# A RegEX or Regular Expression is a sequesnce or characters that forms a search pattern.
# It is a super-search tool for text

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$",txt)
print(x)
if x:
    print("YES! We have a match")

else:
    print("No match")



