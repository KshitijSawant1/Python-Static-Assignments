"""
Name:-Kshitij Sawant
Dept:-Computer Engineering
Batch:- CO B-1
Phone Number :- 9820402146
"""


import package_assignment.filecreation as fc
import package_assignment.fileread as fr
import package_assignment.filewrite as fw
import package_assignment.fileappend as fa
import package_assignment.filedelete as fd


def menu():
    print("_____________________________________")
    print("|        File Handling Menu         |")
    print("|___________________________________|")
    print("|  1. Create a new file             |")
    print("|___________________________________|")
    print("|  2. Read a file                   |")
    print("|___________________________________|")
    print("|  3. Write to a file               |")
    print("|___________________________________|")
    print("|  4. Append to a file              |")
    print("|___________________________________|")
    print("|  5. Delete a file                 |")
    print("|___________________________________|")
    print("|  6. Exit                          |")
    print("|___________________________________|")
    choice = input("|   Enter your choice (1-6):")
    return choice


while True:
    choice = menu()
    if choice == '1':
        fc.creation_of_file()
    elif choice == '2':
        fr.reading_of_file()
    elif choice == '3':
        fw.writing_of_file()
    elif choice == '4':
        fa.appending_of_file()
    elif choice == '5':
        fd.deleting_of_file()
    elif choice == '6':
        print("_____________________________________")
        print("|           Exiting program         |")
        print("|___________________________________|")
        break
    else:
        print("_____________________________________")
        print("| Invalid choice. Please try again. |")
        print("|___________________________________|")
    print("\n")
