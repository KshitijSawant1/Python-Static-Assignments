import math
print()


class LessThan0Error(Exception):
    def __init__(self, args):
        super().__init__(args)
    pass


def Start():
    print("|                                                                           |")
    choice = input("| ENTER OPRATION NUMBER TO PERFOM : ")
    try:
        match choice:
            case '1':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Addition                                                               |")
                Number1 = int(input("| Enter First Number : "))
                Number2 = int(input("| Enter Second Number : "))
                if Number1 <= 0 or Number2 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
                    result = Number1+Number2
                    print(f"| Result of Addition = {result}")
            case '2':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Subtraction                                                            |")
                Number1 = int(input("| Enter First Number : "))
                Number2 = int(input("| Enter Second Number : "))
                if Number1 <= 0 or Number2 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
                    result = Number1-Number2
                    print(f"| Result of Subtraction = {result}")
            case '3':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Multiplication                                                         |")
                Number1 = int(input("| Enter First Number : "))
                Number2 = int(input("| Enter Second Number : "))
                if Number1 <= 0 or Number2 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
                    result = Number1*Number2
                    print(f"| Result of Multiplication = {result}")
            case '4':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Division                                                               |")
                Number1 = int(input("| Enter First Number : "))
                Number2 = int(input("| Enter Second Number : "))
                if Number1 <= 0 or Number2 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
                    result = Number1/Number2
                    print(f"| Result of Division = {result}")
            case '5':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Floor Division                                                         |")
                Number1 = int(input("| Enter First Number : "))
                Number2 = int(input("| Enter Second Number : "))
                if Number1 <= 0 or Number2 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
                    result = Number1//Number2
                    print(f"| Result of Floor Division = {result}")
            case '6':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Modulus Division                                                       |")
                Number1 = int(input("| Enter First Number : "))
                Number2 = int(input("| Enter Second Number : "))
                if Number1 <= 0 or Number2 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
                    result = Number1 % Number2
                    print(f"| Result of Modulus Division = {result}")
            case '7':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Exponentation                                                          |")
                Number1 = int(input("| Enter First Number : "))
                Number2 = int(input("| Enter Second Number : "))
                if Number1 <= 0 or Number2 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:

                    print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
                    result = Number1**Number2
                    print(f"| Result of Exponentation = {result}")
            case '8':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Cube                                                                   |")
                Number1 = int(input("| Enter Number : "))
                if Number1 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(f"| Number = {Number1}")
                    result = Number1*Number1*Number1
                    print(f"| Result of Cube = {result}")
            case '9':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Square                                                                 |")
                Number1 = int(input("| Enter Number : "))
                if Number1 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(f"| Number = {Number1}")
                    result = Number1*Number1
                    print(f"| Result of Square = {result}")
            case '10':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Square Root                                                            |")
                Number1 = int(input("| Enter Number : "))
                if Number1 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(f"| Number = {Number1}")
                    result = math.sqrt(Number1)
                    print(f"| Result of Square Root = {result}")
            case '11':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Logical AND                                                            |")
                Number1 = int(input("| Enter First Number : "))
                Number2 = int(input("| Enter Second Number : "))
                if Number1 <= 0 or Number2 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
                    result = Number1 and Number2
                    print(f"| Result of Logical AND = {result}")
            case '12':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Logical OR                                                             |")
                Number1 = int(input("| Enter First Number : "))
                Number2 = int(input("| Enter Second Number : "))
                if Number1 <= 0 or Number2 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
                    result = Number1 or Number2
                    print(f"| Result of Logical OR = {result}")
            case '13':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Logical NOT                                                            |")
                Number1 = int(input("| Enter Number : "))
                if Number1 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(f"| Number = {Number1}")
                    result = not Number1
                    print(f"| Result of Logical NOT = {result}")
            case '14':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Bitwsie AND                                                            |")
                Number1 = int(input("| Enter First Number : "))
                Number2 = int(input("| Enter Second Number : "))
                if Number1 <= 0 or Number2 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
                    result = Number1 & Number2
                    print(f"| Result of Bitwise AND = {result}")
            case '15':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Bitwise NOT                                                            |")
                Number1 = int(input("| Enter First Number : "))
                if Number1 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(f"| Number = {Number1}")
                    result = ~Number1
                    print(f"| Result of Bitwise NOT = {result}")
            case '16':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Bitwise OR                                                             |")
                Number1 = int(input("| Enter First Number : "))
                Number2 = int(input("| Enter Second Number : "))
                if Number1 <= 0 or Number2 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
                    result = Number1 | Number2
                    print(f"| Result of Bitwise OR = {result}")
            case '17':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Bitwise XOR                                                            |")
                Number1 = int(input("| Enter First Number : "))
                Number2 = int(input("| Enter Second Number : "))
                if Number1 <= 0 or Number2 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
                    result = Number1 ^ Number2
                    print(f"| Result of Bitwsie XOR = {result}")
            case '18':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Bitwise Shift Left                                                     |")
                Number1 = int(input("| Enter First Number : "))
                Number2 = int(input("| Enter Number of Bits to Shift Left : "))
                if Number1 <= 0 or Number2 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(
                        f"| Number 1 = {Number1} and Number of Bits to Shift Left are = {Number2}")
                    result = Number1 << Number2
                    print(f"| Result of Bitwise Shift Left = {result}")
            case '19':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Bitwise Shift Right                                                    |")
                Number1 = int(input("| Enter First Number : "))
                Number2 = int(input("| Enter Number of Bits to Shift Right: "))
                if Number1 <= 0 or Number2 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(
                        f"| Number 1 = {Number1} and Number of Bits to Shift Right are = {Number2}")
                    result = Number1 >> Number2
                    print(f"| Result of Bitwise Shift Left = {result}")
            case '20':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Equal Values or Not                                                    |")
                Number1 = int(input("| Enter First Number : "))
                Number2 = int(input("| Enter Second Number : "))
                if Number1 <= 0 or Number2 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
                    if (Number1 == Number2):
                        result = "True Values are Equal"
                    else:
                        result = "False Values are not Eqaul"
                print(f"| Result of Eqaul Values or Not = {result}")
            case '21':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Greater than (or Equal)                                                |")
                Number1 = int(input("| Enter First Number : "))
                Number2 = int(input("| Enter Second Number : "))
                if Number1 <= 0 or Number2 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
                    if (Number1 > Number2):
                        result = "Number 1 is Greater than Number 2"
                    elif Number1 == Number2:
                        result = "Number 1 is Equal to Number 2"
                    elif Number2 > Number1:
                        result = "Number 2 is Greater than Number 1"
                print(f"| Result of Greater than (or Equal) = {result}")
            case '22':
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "| => Less than (or Equal)                                                   |")
                Number1 = int(input("| Enter First Number : "))
                Number2 = int(input("| Enter Second Number : "))
                if Number1 <= 0 or Number2 <= 0:
                    raise LessThan0Error("Entered number should be positive")
                else:
                    print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
                    if (Number1 < Number2):
                        result = "Number 1 is Less than Number 2"
                    elif Number1 == Number2:
                        result = "Number 1 is Equal to Number 2"
                    elif Number2 < Number1:
                        result = "Number 2 is Less than Number 1"
                print(f"| Result of Less than (or Equal) = {result}")

            case _:
                print(
                    "|---------------------------------------------------------------------------|")
                print(
                    "|                    !!!INVALID OPERATOR NUMBER !!!                         |")
                print(
                    "|                                                                           |")
    except ValueError:
        print(
            "|---------------------------------------------------------------------------|")
        print(
            "|                     !!! INVALID INPUT !!!                                 |")
    except LessThan0Error as ltte:
        print(
            "|---------------------------------------------------------------------------|")
        print(
            f"| !!!   {type(ltte).__name__} : {ltte.args[0]} !!!")


# Exit function:-
def Exit():
    print("|---------------------------------------------------------------------------|")
    print("|               ---- THANK YOU FOR USING CALCULATOR ----                    |")
    print("|---------------------------------------------------------------------------|")

    print()
