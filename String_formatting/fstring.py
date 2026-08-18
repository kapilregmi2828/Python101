# f-string allows you to format selected parts of a string. 

txt = f"The price is 49 dollars"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

txt2 = f"The price is {price:.2f} dollars"
print(txt2)

price2 = 1000
txt3 = f"The price is {price2:,} dollars"
print(txt3)

# if - else condition in f string

price3 = 49
txt4 = f"It is very {'Expensive' if price3 > 50 else 'Cheap'}"
print(txt4)

# format() method is also used to format string but the syntax is bit different. 

rate = 49
sentence = "The price is {} dollars"
print(sentence.format(rate))

line = "The price is {:.2f} dollars"
print(line.format(rate))