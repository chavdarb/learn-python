msg = "It's a sunny day"
quote = 'She said, "Hello World!"'
multiline_string = """This is a multiline string.
It can span multiple lines.
It preserves the line breaks and spacing."""
my_str = 'Hello world'
my_str2 = 'Hello' + ' ' + 'world'  # Concatenation
my_str3 = 'Hello' * 3  # Repetition
name = "John Doe"
age = 26
name_and_age = f"{name} is {age} years old."  # f-string for formatting

print(msg)
print(quote)
print(multiline_string)
print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False
print(len(my_str))
print(my_str[0],my_str[6]) # H w
print(my_str[-1])  # d
print(my_str[0:5])  # Hello
print(my_str[6:])   # world
print(my_str[:5])   # Hello
print(my_str[:])  # Hello world
print(my_str[::2])  # Hlo ol
print(my_str[::-1])  # dlrow olleH
print(my_str.upper())  # HELLO WORLD
print(my_str.lower())  # hello world
print(my_str2)  # Hello world
print(my_str3)  # HelloHelloHello
print(my_str.replace('world', 'Python'))  # Hello Python
print(my_str.split())  # ['Hello', 'world']
print(my_str.strip())  # Hello world (removes leading/trailing whitespace)
print("John is " + str(age) + " years, old.")  # John is 26 years old.
print(name_and_age)  # John Doe is 26 years old.
print(",".join(['one','two','three']))
print("Hello World".startswith("Hello"))
print("Hello World".endswith("World"))
print("Hello World".find("World"))
print("Hello World".count("o"))
print("HELLO WORLD".isupper())
print("hello world".islower())
print("hello world".title())