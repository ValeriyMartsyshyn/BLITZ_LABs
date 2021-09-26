#task 13
alist= ["q", "", "w", "e", ""]
a=[]
for string in alist:
    if (string!=""):
        a.append(string)
print(a)


#task 14
n=int(input())
def sumDigits(n):
    sum=0
    while(n!=0):
        sum=sum+int(n%10)
        n=int(n/10)
    return sum
print(sumDigits(n))


#task 15
def is_sorted(mylist):
    return mylist==sorted(mylist)
mylist=input("Enter a list: ")
mylist=mylist.split()
print(is_sorted(mylist))


