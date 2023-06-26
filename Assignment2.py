"""
Name:-Kshitij Sawant
Dept:-Computer Engineering
Batch:- CO B-1
Phone Number :- 9820402146

Python divides the operators in the following groups:
    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators
"""
#Arithematic Operators
x=10
y=20
print("--------------------------------------------------------------------------")
print("Arithematic Operators")
#Addition
print(f"Addition (+) of X ={x} and Y={y} is {x+y}")
#subtraction
print(f"Subtracion (-) of X ={x} and Y={y} is {x-y}")
#Multiplication
print(f"Multiplication (*) of X ={x} and Y={y} is {x*y}")
#Division
print(f"Division (/) of X ={x} and Y={y} is {x/y}")
#Modulus
print(f"Modulus (%) of X ={x} and Y={y} is {x%y}")
#Exponent
print(f"Exponent (**) of X ={x} and Y={y} is {x**y}")
#Floor Division
print(f"Floor Division (//) of X ={x} and Y={y} is {x//y}")
print("--------------------------------------------------------------------------")

#Assignment operators
print("Assignment operators")
print(f"X = {x}")
x = x + 5	
print(f"x += 5 = {x}")
x = x - 5	
print(f"x -= 5 = {x}")
x = x * 5	
print(f"x *= 5 = {x}")
x = x / 5	
print(f"x /= 5 = {x}")
x = x % 5	
print(f"x %= 5 = {x}")
x = x // 5	
print(f"x //= 5 = {x}")
x = x ** 5	
print(f"x *= 5 = {x}")
print("--------------------------------------------------------------------------")

#Comparison Operators
print("Comparison Operators")
#Equal to (==)
print(f"Equal to (==) of X = {x} and Y = {y} is {x==y}")
#Not Eqaul to (!=)
print(f"Not Eqaul to (!=)of X = {x} and Y = {y} is {x!=y}")
# Greater Than (>)
print(f"Greater Than (>) of X = {x} and Y = {y} is {x>y}")
# Less Than (<)
print(f"Less Than (<) of X = {x} and Y = {y} is {x<y}")
# Greater Than Eqaul to (>=)
print(f"Greater Than Eqaul to (>=) of X = {x} and Y = {y} is {x>=y}")
# Less Than Equal to (<=)
print(f"Less Than Equal to (<=) of X = {x} and Y = {y} is {x<=y}")
print("--------------------------------------------------------------------------")

#Logical Operator
print("Logical Operator")
# and
print(f"And of X = {x} and Y = {y} is {x and y}")
# or 
print(f"Or of X = {x} and Y = {y} is {x or y}")
# not
print(f"Not of X = {x} is {not x}")
print(f"Not of Y = {y} is {not y}")
print("--------------------------------------------------------------------------")

#Identity Operator
print("Identity Opertor")
a=["C++","Java","Python","React"]
b=["C++","Java","Python","React"]
print(f"a = {a}")
print(f"b = {b}")
# is
print(f"Is will return true if both operands are same {a is b}")
# is not
print(f"Is Not will return true if both operands are not same {a is not b}")
print("--------------------------------------------------------------------------")

#Membership Operator
print("Membership Opertor")
c=["C++","Java","Python","React"]
print(f"C = {c}")
# in
print(f"In will return true if value passed is present")
print("Python" in c)
# not in
print(f"Not In will return true if value passed is not present")
print("SQL" in c)
print("--------------------------------------------------------------------------")

# Bitwise Operator
x=10
y=8
print("Bitwise Operator")
# AND
print(f"AND of X = {x} and Y = {y} is {x & y}")
# OR
print(f"OR of X = {x} and Y = {y} is {x | y}")
# NOT
print(f"NOT of X = {x} is {~x}")
print(f"NOT of Y = {y} is {~y}")
# XOR
print(f"XOR of X = {x} and Y = {y} is {x ^ y}")
# SHIFT LEFT
print(f"SHIFT LEFT of X = {x} by 2 is {x << 2}")
# SHIFT RIGHT
print(f"SHIFT RIGHT of Y = {y} by 2 is {y >> 2}")
print("--------------------------------------------------------------------------")