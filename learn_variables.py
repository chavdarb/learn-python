# Example of variable assignment in Python
name = 'John Doe'
sentence = "My name is "
age = 25
pi = 3.14
boolean_variable = True
set_variable = {1, 2, 3}
dictionary_variable = {"key1": "value1", "key2": 42}
tuple_variable = (1, 2, 3)
range_variable = range(5)
list_variable = [1, 2, 3, 4, "Five"]
none_variable = None

# Printing the variables

print("Hello, Chavdar!")  
print(sentence, name, "!")
print("I am", age, "years old.")
print("Integer variable:", age, type(age))
print("String variable:", name, type(name))
print("Float variable:", pi, type(pi))
print("Boolean variable:", boolean_variable, type(boolean_variable))
print("Set variable:", set_variable, type(set_variable))
print("Dictionary variable:", dictionary_variable, type(dictionary_variable))
print("Tuple variable:", tuple_variable, type(tuple_variable))
print("Range variable:", range_variable, type(range_variable))
print("List variable:", list_variable, type(list_variable))
print("None variable:", none_variable, type(none_variable))

print(isinstance('Hello world', str)) # True
print(isinstance(True, bool)) # True
print(isinstance(42, int)) # True
print(isinstance('John Doe', int)) # False