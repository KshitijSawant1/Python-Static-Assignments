"""
Name:-Kshitij Sawant
Dept:-Computer Engineering
Batch:- CO B-1
Phone Number :- 9820402146
"""
def ds(roll_no,name):
    global List 
    global Tuple
    global Set
    global Dictionary
    List=[roll_no,name]
    Tuple=(roll_no,name)
    Set={roll_no,name}
    Dictionary={"Roll no.": roll_no , "Name":name}


def printdatastructure():
    print("INSIDE PRINT FUNCTION")
    print("\nList : ",List,"\n")
    print("Tuple : ",Tuple,"\n")
    print("Set : ",Set,"\n")
    print("Dictionary : ",Dictionary,"\n")

def updatedatastructure():
    print("INSIDE PRINT FUNCTION")
    rn=int(input("Enter the roll no : "))
    nm=input("Enter the name    : ")
    ds(rn,nm)
    List.append("Computer Engineering");
    List.pop(0)
    List.insert(0,101)
    Set.add("Computer Engineeering")
    Dictionary.update({"Department":"Computer Engineering"})

# Driver code:-
ds(101,"KAIZEN")
printdatastructure()
updatedatastructure()
printdatastructure()