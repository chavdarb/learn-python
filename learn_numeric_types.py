import sys

my_int_1 = 56
my_int_2 = -4
n = 1000000000000023323

print(type(my_int_1)) # <class 'int'>
print(type(my_int_2)) # <class 'int'>
print(type(n)) # <class 'int'>
print(n.bit_length()) # bits needed to represent n in binary, excluding the sign and leading zeros
print(sys.int_info) # Information about the internal representation of integers in Python
print((n.bit_length() + sys.int_info.bits_per_digit - 1)//sys.int_info.bits_per_digit)
print(sys.getsizeof(n)) # Size in bytes

my_int_1 = 56
my_int_2 = 12

sum_ints = my_int_1 + my_int_2
print('Integer Addition:', sum_ints) # Integer Addition: 68
my_int_1 = 56
my_int_2 = 12

# Subtraction
diff_ints = my_int_1 - my_int_2
print('Integer Subtraction:', diff_ints) # Integer Subtraction: 44

my_int_1 = 56
my_int_2 = 12

# Division
div_ints = my_int_1 / my_int_2
print('Integer Division:', div_ints) # Integer Division: 4.666666666666667

print(sys.float_info)

my_float_1 = -12.0
my_float_2 = 4.9

print(type(my_float_1)) # <class 'float'>
print(type(my_float_2)) # <class 'float'>

my_float_1 = 5.4
my_float_2 = 12.0

float_addition = my_float_1 + my_float_2
print('Float Addition:', float_addition) # Float Addition: 17.4

my_float_1 = 5.4
my_float_2 = 12.0

float_subtraction = my_float_2 - my_float_1
print('Float Subtraction:', float_subtraction) # Float Subtraction: 6.6

my_float_1 = 5.4
my_float_2 = 12.0

float_multiplication = my_float_2 * my_float_1
print('Float Multiplication:', float_multiplication) # Float Multiplication: 64.80000000000001

my_float_1 = 5.4
my_float_2 = 12.0

float_division = my_float_2 / my_float_1
print('Float Division:', float_division) # Float Division: 2.222222222222222

my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float

print(sum_int_and_float) # 61.4
print(type(sum_int_and_float)) # <class 'float'>

my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1

print('Integer Modulo:', mod_ints) # Integer Modulo: 8
print('Float Modulo:', mod_floats) # Float Modulo: 1.1999999999999993

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print('Integer Floor Division:', floor_div_ints) # Integer Floor Division: 4
print('Float Floor Division:', floor_div_floats) # Float Floor Division: 2.0

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print('Integer Exponentiation:', exp_ints) # Integer Exponentiation: 951166013805414055936
print('Float Exponentiation:',  exp_floats) # Float Exponentiation: 614787626.1765089

my_int_1 = 56
my_float_1 = float(my_int_1)
my_int2 = int(my_float_1)

print(my_int_1)
print(my_float_1)  # 56.0
print(type(my_float_1))  # <class 'float'>
print(my_int2)  # 56
print(type(my_int2))  # <class 'int'>

my_str_int = '45'
my_str_float = '7.8'

converted_int = int(my_str_int)
converted_float = float(my_str_float)
converted_int2 = int(float(my_str_float))
rounded_int2 = round(converted_float)


print(converted_int, type(converted_int))  # 45 <class 'int'>
print(converted_float, type(converted_float))  # 7.8 <class 'float'>
print(converted_int2, type(converted_int2))  # 7 <class 'int'>
print(rounded_int2, type(rounded_int2))  # 8 <class 'int'>

float_big = 1.23456789
float_rounded = round(float_big, 2)
print(float_big)
print(float_rounded)  

num = -15

absolute_value = abs(num)
print(absolute_value) # 15

result_1 = pow(2, 3)  # Equivalent to 2 ** 3
print(result_1)  # 8

result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
print(result_2)  # 3

my_var = 10
my_var += 5

print(my_var) # 15

count = 14
count -= 3

print(count) # 11

product = 65
product *= 7

print(product) # 455

price = 100
price /= 4

print(price) # 25.0

total_pages = 23
total_pages //= 5

print(total_pages) # 4

bits = 35
bits %= 2

print(bits) # 1

power = 2
power **= 3

print(power) # 8

greet = 'Hello'
greet += ' World'

print(greet) # Hello World

greet = 'Hello'
greet *= 3

print(greet) # HelloHelloHello