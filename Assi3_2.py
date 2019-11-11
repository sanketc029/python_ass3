
#to find the maximum no from list
def findmax(lst):
    print("The maximum no is ",max(lst))


lst =[]
no=int(input("print enter the limit if list"))
for i in range(no):
    ele=int(input())
    lst.append(ele)

findmax(lst)
