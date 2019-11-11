
#to find the minimum no from list
def findmin(lst):
    print("The minimum no ",min(lst))

lst=[]
no=int(input("Enter the limits"))
for i in range(no):
    ele=int(input())
    lst.append(ele)
print(lst)

findmin(lst)