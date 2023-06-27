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
# Program demonstrating break, pass, continue, for-else, and while-else
print()
# Break statement
print("Break statement")
for num in range(1, 10):
    if num == 5:
        break
    print(num)
    print("Shown the demonstration of break statement")
print()

# Pass statement
print("Pass statement")
for letter in 'KAIZEN':
    if letter == 'Z':
        pass
    print('Current Letter:', letter)
    print("Shown the demonstration of pass statement")
print()

# Continue statement
print("Continue statment")
for num in range(1, 10):
    if num == 5:
        continue
    print(num)
    print("Shown the demonstration of continue statement")
print()

# For loop with else
print("For loop with else")
for num in range(1, 10):
    print(num*num)
else:
    print("Shown the demonstration of for loop with else successfully!")
print()

# While loop with else
print("While loop with else")
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Shown the demonstration of while loop with else successfully !")
