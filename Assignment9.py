# Program:-
import calc as cl

print("|---------------------------------------------------------------------------|")
print("|                             CALCULATOR                                    |")
print("|---------------------------------------------------------------------------|")
print("| => CHOOSE THE OPERTION TO PERFORM (OPERATION NUMBER)                      |")
print("|---------------------------------------------------------------------------|")
print("| Arithematic Operations                                                    |")
print("|---------------------------------------------------------------------------|")
print("|    1) Addition                          2) Subtraction                    |")
print("|    3) Multiplication                    4) Division                       |")
print("|    5) Floor Division                    6) Modulus Division               |")
print("|    7) Exponentation                     8) Cube                           |")
print("|    9) Square                           10) Square Root                    |")
print("|---------------------------------------------------------------------------|")
print("| Logical Operations                                                        |")
print("|---------------------------------------------------------------------------|")
print("|    11) Logical AND                                                        |")
print("|    12) Logical OR                                                         |")
print("|    13) Logical NOT                                                        |")
print("|---------------------------------------------------------------------------|")
print("| Bitwsie Operation                                                         |")
print("|---------------------------------------------------------------------------|")
print("|    14) Bitwise AND                     15) Bitwise NOT                    |")
print("|    16) Bitwise OR                      17) Bitwise XOR                    |")
print("|    18) Bitwise Shift Left              19) Bitwise Shift Right            |")
print("|---------------------------------------------------------------------------|")
print("| Comparision Operations                                                    |")
print("|---------------------------------------------------------------------------|")
print("|    20) Equal Values or Not                                                |")
print("|    21) Greater than (or Eqaul)                                            |")
print("|    22) Less than (or Eqaul)                                               |")
print("|---------------------------------------------------------------------------|")
cl.Start()
StayOrLeave = 'Y'
while (StayOrLeave != 'N'):
    print("|---------------------------------------------------------------------------|")
    print("|                                                                           |")
    print("|     Y) COUNTINUE                        N) EXIT                           |")
    ch = input("|     => ENTER THE CHOICE : ")
    print("|---------------------------------------------------------------------------|")
    match ch:
        case 'Y':
            cl.Start()
        case 'y':
            cl.Start()
        case 'N':
            cl.Exit()
        case 'n':
            StayOrLeave = 'N'
            cl.Exit()
        case _:
            print(
                "|---------------------------------------------------------------------------|")
            print(
                "|                    !!!INVALID CHOICE !!!                                  |")
            print(
                "|                                                                           |")
