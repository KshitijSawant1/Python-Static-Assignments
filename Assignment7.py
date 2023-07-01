"""
Name:-Kshitij Sawant
Dept:-Computer Engineering
Batch:- CO B-1
Phone Number :- 9820402146
"""
import os
def fileFunction(file="Information.txt"):
    try:
        File=open(file,"a+t")
        File.writelines(["Roll no. : 10\n","Name : KAIZEN\n","Class : SYCO-A\n"])
        File.seek(0)
        print(f"Information : \n{File.readlines()}\n")
    except FileNotFoundError:
        print(f"File not present at given path.")
    except Exception:
        print(f"Something went wrong.")
    finally:
        return;
fileFunction();
