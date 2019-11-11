
# the programm is addition of all list members
def sum(lst):
    sum=0
    for i in range(len(lst)):
        sum=sum+lst[i]
    print("Addition of all list elements ",sum)



no = int(input("Enter the number"))
lst=[]
for i in range(0,no):
    ele=int(input())
    lst.append(ele)
sum(lst)