# while loop is used to iterate a code block as long as the condition is true. 
# we can use break to come out of loop even if condition is true.
# we use continue to skip a case and continue other cases. 

i = 0
while i < 6:
   print(i)
   if i == 3:
      break # break condtion 
   i += 1

j = 0
while j < 6:
   j += 1
   if j == 3:
      continue # continue
   print(j)