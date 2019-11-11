
# the main file
#the programm is print the addition of prime no's from list
from Assi_3.Assi3_5_2 import chkprime

def acceptno():
    no=int(input("Enter the no"))
    arr =[]
    for i in range(no):
        arr.append(int(input()))

    chkprime(arr)

acceptno()

