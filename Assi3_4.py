#to find the x no of occurence from list

def searchno(lst,x):
    cnt=0
    sec=[]
    for i in range(len(lst)):
        if lst[i]==x:
            cnt=cnt+1
    print("The count of ",x ,"in list is",cnt)

lst=[]
no=int(input("Enter the list limit"))
for i in range(no):
    lst.append(int(input()))
print("The list is",lst)
x=int(input("Enter no for search in list"))
searchno(lst,x)
