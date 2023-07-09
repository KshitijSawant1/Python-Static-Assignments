def reading_of_file():
    print("|___________________________________|")
    filename = input("| Enter the file name : ")
    print("|___________________________________|")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("|___________________________________|")
            print("|  File content:                    |")
            print("| "+content)
            print("|___________________________________|")

    except:
        print("|___________________________________|")
        print("|        Error reading file         |")
        print("|___________________________________|")
