# this will be an example of *args and **kwargs

def fun1(title, *args, **kwargs):
    print("Title:",title)
    print("Positional Arguments:", args)
    print("Keyword Arguments:", kwargs)

fun1("User Info", "Kapil", "Regmi", age = 18, city = 'Dallas')

# this is a great example of *args, **kwargs, and regular argumenets. 