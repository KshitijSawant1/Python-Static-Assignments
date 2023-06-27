import math
print()

def Start():
    print("|                                                                           |")
    choice =input("| ENTER OPRATION NUMBER TO PERFOM : ")
    
    match choice:
        case '1':
            print("|---------------------------------------------------------------------------|")
            print("| => Addition                                                               |")
            Number1=int(input("| Enter First Number : "))
            Number2=int(input("| Enter Second Number : "))
            print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
            result=Number1+Number2
            print(f"| Result of Addition = {result}")        
        case '2':
            print("|---------------------------------------------------------------------------|")
            print("| => Subtraction                                                            |")
            Number1=int(input("| Enter First Number : "))
            Number2=int(input("| Enter Second Number : "))
            print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
            result=Number1-Number2
            print(f"| Result of Subtraction = {result}")  
        case '3':
            print("|---------------------------------------------------------------------------|")
            print("| => Multiplication                                                         |")
            Number1=int(input("| Enter First Number : "))
            Number2=int(input("| Enter Second Number : "))
            print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
            result=Number1*Number2
            print(f"| Result of Multiplication = {result}")    
        case '4':
            print("|---------------------------------------------------------------------------|")
            print("| => Division                                                               |")
            Number1=int(input("| Enter First Number : "))
            Number2=int(input("| Enter Second Number : "))
            print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
            result=Number1/Number2
            print(f"| Result of Division = {result}")     
        case '5':
            print("|---------------------------------------------------------------------------|")
            print("| => Floor Division                                                         |")
            Number1=int(input("| Enter First Number : "))
            Number2=int(input("| Enter Second Number : "))
            print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
            result=Number1//Number2
            print(f"| Result of Floor Division = {result}")     
        case '6':
            print("|---------------------------------------------------------------------------|")
            print("| => Modulus Division                                                       |")
            Number1=int(input("| Enter First Number : "))
            Number2=int(input("| Enter Second Number : "))
            print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
            result=Number1%Number2
            print(f"| Result of Modulus Division = {result}")     
        case '7':
            print("|---------------------------------------------------------------------------|")
            print("| => Exponentation                                                         |")
            Number1=int(input("| Enter First Number : "))
            Number2=int(input("| Enter Second Number : "))
            print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
            result=Number1**Number2
            print(f"| Result of Exponentation = {result}")     
        case '8':
            print("|---------------------------------------------------------------------------|")
            print("| => Cube                                                                   |")
            Number1=int(input("| Enter Number : "))
            print(f"| Number = {Number1}")
            result=Number1*Number1*Number1
            print(f"| Result of Cube = {result}")     
        case '9':
            print("|---------------------------------------------------------------------------|")
            print("| => Square                                                                 |")
            Number1=int(input("| Enter Number : "))
            print(f"| Number = {Number1}")
            result=Number1*Number1
            print(f"| Result of Square = {result}")     
        case '10':
            print("|---------------------------------------------------------------------------|")
            print("| => Square Root                                                            |")
            Number1=int(input("| Enter Number : "))
            print(f"| Number = {Number1}")
            result=math.sqrt(Number1)
            print(f"| Result of Square Root = {result}")        
        case '11':
            print("|---------------------------------------------------------------------------|")
            print("| => Logical AND                                                            |")
            Number1=int(input("| Enter First Number : "))
            Number2=int(input("| Enter Second Number : "))
            print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
            result=Number1 and Number2
            print(f"| Result of Logical AND = {result}")     
        case '12':
            print("|---------------------------------------------------------------------------|")
            print("| => Logical OR                                                             |")
            Number1=int(input("| Enter First Number : "))
            Number2=int(input("| Enter Second Number : "))
            print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
            result=Number1 or Number2
            print(f"| Result of Logical OR = {result}")     
        case '13':
            print("|---------------------------------------------------------------------------|")
            print("| => Logical NOT                                                            |")
            Number1=int(input("| Enter Number : "))
            print(f"| Number = {Number1}")
            result=not Number1
            print(f"| Result of Logical NOT = {result}")     
        case '14':
            print("|---------------------------------------------------------------------------|")
            print("| => Bitwsie AND                                                            |")
            Number1=int(input("| Enter First Number : "))
            Number2=int(input("| Enter Second Number : "))
            print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
            result=Number1 & Number2
            print(f"| Result of Bitwise AND = {result}")     
        case '15':
            print("|---------------------------------------------------------------------------|")
            print("| => Bitwise NOT                                                            |")
            Number1=int(input("| Enter First Number : "))
            print(f"| Number = {Number1}")
            result=~Number1
            print(f"| Result of Bitwise NOT = {result}")     
        case '16':
            print("|---------------------------------------------------------------------------|")
            print("| => Bitwise OR                                                             |")
            Number1=int(input("| Enter First Number : "))
            Number2=int(input("| Enter Second Number : "))
            print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
            result=Number1 | Number2
            print(f"| Result of Bitwise OR = {result}")     
        case '17':
            print("|---------------------------------------------------------------------------|")
            print("| => Bitwise XOR                                                            |")
            Number1=int(input("| Enter First Number : "))
            Number2=int(input("| Enter Second Number : "))
            print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
            result=Number1 ^ Number2
            print(f"| Result of Bitwsie XOR = {result}")     
        case '18':
            print("|---------------------------------------------------------------------------|")
            print("| => Bitwise Shift Left                                                     |")
            Number1=int(input("| Enter First Number : "))
            Number2=int(input("| Enter Number of Bits to Shift Left : "))
            print(f"| Number 1 = {Number1} and Number of Bits to Shift Left are = {Number2}")
            result=Number1 << Number2
            print(f"| Result of Bitwise Shift Left = {result}")     
        case '19':
            print("|---------------------------------------------------------------------------|")
            print("| => Bitwise Shift Right                                                    |")
            Number1=int(input("| Enter First Number : "))
            Number2=int(input("| Enter Number of Bits to Shift Right: "))
            print(f"| Number 1 = {Number1} and Number of Bits to Shift Right are = {Number2}")
            result=Number1 >> Number2
            print(f"| Result of Bitwise Shift Left = {result}")    
        case '20':
            print("|---------------------------------------------------------------------------|")
            print("| => Equal Values or Not                                                    |")
            Number1=int(input("| Enter First Number : "))
            Number2=int(input("| Enter Second Number : "))
            print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
            if(Number1==Number2):
                result="True Values are Equal"
            else:
                result="False Values are not Eqaul"
            print(f"| Result of Eqaul Values or Not = {result}")     
        case '21':
            print("|---------------------------------------------------------------------------|")
            print("| => Greater than (or Equal)                                                |")
            Number1=int(input("| Enter First Number : "))
            Number2=int(input("| Enter Second Number : "))
            print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
            if(Number1>Number2):
                result="Number 1 is Greater than Number 2"
            elif Number1==Number2:
                result="Number 1 is Equal to Number 2"
            elif Number2>Number1:
                result="Number 2 is Greater than Number 1"
            print(f"| Result of Greater than (or Equal) = {result}")    
        case '22':
            print("|---------------------------------------------------------------------------|")
            print("| => Less than (or Equal)                                                   |")
            Number1=int(input("| Enter First Number : "))
            Number2=int(input("| Enter Second Number : "))
            print(f"| Number 1 = {Number1} and Number 2 = {Number2}")
            if(Number1<Number2):
                result="Number 1 is Less than Number 2"
            elif Number1==Number2:
                result="Number 1 is Equal to Number 2"
            elif Number2<Number1:
                result="Number 2 is Less than Number 1" 
            print(f"| Result of Less than (or Equal) = {result}")    

        case _:
            print("|---------------------------------------------------------------------------|")
            print("|                    !!!INVALID OPERATOR NUMBER !!!                         |");
            print("|                                                                           |")
                                  

# Exit function:-
def Exit():
    print("|---------------------------------------------------------------------------|")
    print("|               ---- THANK YOU FOR USING CALCULATOR ----                    |")
    print("|---------------------------------------------------------------------------|")

    print();

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
print("|     Y) COUNTINUE                        N) EXIT                           |")
print("|---------------------------------------------------------------------------|")
print("| Comparision Operations                                                    |")
print("|---------------------------------------------------------------------------|")
print("|    20) Equal Values or Not                                                |")
print("|    21) Greater than (or Eqaul)                                            |")
print("|    22) Less than (or Eqaul)                                               |")
print("|---------------------------------------------------------------------------|")
Start();
StayOrLeave='Y';
while(StayOrLeave!='N'):
    print("|---------------------------------------------------------------------------|")
    print("|                                                                           |")
    print("|     Y) COUNTINUE                        N) EXIT                           |")
    ch=input("|     => ENTER THE CHOICE : ")
    print("|---------------------------------------------------------------------------|")
    match ch:
        case 'Y':
            Start();
        case 'y':
            Start();
        case 'N':
            Exit(); 
        case 'n':
            StayOrLeave='N'
            Exit();
        case _:
            print("|---------------------------------------------------------------------------|")
            print("|                    !!!INVALID CHOICE !!!                                  |");  
            print("|                                                                           |")
                
