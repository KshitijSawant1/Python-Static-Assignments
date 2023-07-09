def creation_of_file():
    print("|___________________________________|")
    filename = input("| Enter the file name : ")
    print("|___________________________________|")

    try:
        with open(filename, 'w') as file:
            print("|___________________________________|")
            print("| File created successfully         |")
            print("|___________________________________|")

    except:
        print("|___________________________________|")
        print("|        Error creating file        |")
        print("|___________________________________|")
