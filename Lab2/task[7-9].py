# task 7#create a list and print it #remove any repeated items and print the result 
list = [0, 0, 1, 2, 2, 2, 3, 1, 3, 1, 3, 1, 4, 5, 6, 5, 4]
print ("The initial list : " +  str(list))
res = []
for i in list:
    if i not in res:
        res.append(i)
print ("The eventual list : " + str(res))

#task 8#create a list#sort the list numerically if True, otherwise sort alphabetically#print the results and "Done"
def mySort(list=[], num=False):
    numerics = []
    alphabets = []
    for sub in list:
        if str(sub).isnumeric():
            numerics.append(sub)
        else:
            alphabets.append(sub)
    if(num)==True:
        return sorted(numerics) + sorted(alphabets)
    return sorted(alphabets) + sorted(numerics)
   
a = ['a', 'b', 1, 'g', 5, 9]  

print(mySort(a, True))
print(mySort(a, False))
print("Done")

# task 9#ask the user to enter an input#print if it is true or false#print if the input is None or NaN
import math
a = input('Enter any positive integer number ')

if isinstance(a, str) and not a.isnumeric() and  a != 'Nan' and a != 'nan' and a!= '':
    print("False")
elif a.isnumeric():
    print("True")
elif a!= '' and math.isnan(float(a)):
    print("it is a Nan value")
else:
    print("it is None value")
