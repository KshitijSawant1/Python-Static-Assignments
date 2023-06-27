"""
Name:-Kshitij Sawant
Dept:-Computer Engineering
Batch:- CO B-1
Phone Number :- 9820402146
"""
print()
print("Input 5 numbers from the user")
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
print()
print("Calculate the sum of all elements")
sum_of_numbers = sum(numbers)
print("Sum of numbers:", sum_of_numbers)

print()
print("Find the smallest number")
smallest_number = min(numbers)
print("Smallest number:", smallest_number)

print()
print("Find the largest number")
largest_number = max(numbers)
print("Largest number:", largest_number)

print()
print("Display list in ascending order")
ascending_order = sorted(numbers)
print("List in ascending order:", ascending_order)

print()
print("Display list in descending order")
descending_order = sorted(numbers, reverse=True)
print("List in descending order:", descending_order)

print()
print("Convert list into tuple")
numbers_tuple = tuple(numbers)
print("List converted to tuple:", numbers_tuple)

print()
print("Delete the list")
del numbers
print("List deleted")
