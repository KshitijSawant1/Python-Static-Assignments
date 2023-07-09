def writing_of_file():
    print("|___________________________________|")
    filename = input("| Enter the file name : ")
    print("|___________________________________|")
    content = input("| Enter the content to write: ")
    print("|___________________________________|")

    try:
        with open(filename, 'w') as file:
            print("|___________________________________|")
            file.write(content)
            print("| Content written successfully      |")
            print("|___________________________________|")

    except:
        print("|___________________________________|")
        print("|        Error writing file         |")
        print("|___________________________________|")
