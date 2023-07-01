import sys
class A:
    def __init__(self,a,b,c):
        self.__a=a
        self._b=b
        self.c=c
    def display(self):
        print()
        print("INSIDE CLASS A")
        print(f"Private variable (__a) = {self.__a}")
        print(f"Protected variable (_b) = {self._b}")
        print(f"Public variable (c) = {self.c}")
        print()
class B(A):
    def display(self):
        print()
        print("INSIDE CLASS B")
        try:
            print(f"Private variable (__a) = {self.__a}")
        except AttributeError as AE:
            print(f"{type(AE).__name__} : PRIVATE MEMBER '__a' INACCESSIBLE ")
        print(f"Protected variable (_b) = {self._b}")
        print(f"Public variable (c) = {self.c}")
        super().display()
        print()
        
Z=B(10,20,30)
Z.display()