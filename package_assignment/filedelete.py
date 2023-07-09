import os


def deleting_of_file():
    print("|___________________________________|")
    filename = input("| Enter the file name : ")
    print("|___________________________________|")
    try:
        os.remove(filename)
        print("|___________________________________|")
        print("| File deleted successfully         |")
        print("|___________________________________|")

    except:
        print("|___________________________________|")
        print("|        Error deleting file        |")
        print("|___________________________________|")
