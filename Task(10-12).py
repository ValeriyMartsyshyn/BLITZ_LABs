#Task 10

dct={'c': 2,
     'r': 3,
     't': 5,
     'x': 21,
     'y': 3,
     'o': 54}
lst_values=[i for i in dct.values()]
max_value=max(lst_values)
lst_keys=[i for i in dct.keys()]
for i in lst_keys:
    if dct[i]==max_value:
        print('answer is: ' + i)
#Task 11
lst = list(input("Enter large int:"))
lens = len(lst)
n = -3
c = 4
while n>=-lens-150:
    lst.insert(n, ',')
    n-=c
while lst[0] == ',':
    lst.pop(0)
k = ''.join(lst)
print(k)

#Task 12
str='abcdefghijklmnopqrstuvwxyz'
for i in range(0,26):
    print(str[i:]+str[:i])

