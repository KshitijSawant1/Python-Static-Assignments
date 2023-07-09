def appending_of_file():
    print("|___________________________________|")
    filename = input("| Enter the file name : ")
    print("|___________________________________|")
    content = input("| Enter the content to append: ")
    print("|___________________________________|")

    try:
        with open(filename, 'a') as file:
            file.write('\n' + content)
            print("|___________________________________|")
            print("| Content appended successfully     |")
            print("|___________________________________|")

    except:
        print("|___________________________________|")
        print("|        Error appending file       |")
        print("|___________________________________|")
