# sub() function replaces the matches with the text of your choice. 

import re
txt = "The rain in Spain"

x = re.sub("\s", "9", txt)
print(x) # The9rain9in9Spain

y = re.sub("\s", "9", txt, 2) # replaces the first 2 occurences only also knows as count parameter
print(y)