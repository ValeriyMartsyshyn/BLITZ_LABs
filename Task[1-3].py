""" Task 1

    Ask the user how many Fibonacci numbers to print
"""
def spaghetti(num):

    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib

number = int(input("How many Fibonacci numbers to print?: "))
print(spaghetti(number))

""" Task 2

    Calculate: ∑𝑘
"""
num_1 = int(input('Enter a number: '))

s = 0 
for i in range(1, num_1+1):
    s += i

print(s)

""" Task 3

    Calculate number of distinct characters in a string using a for loop
"""
str_tmp = input('Enter The sentence: ')

#Loop for except " "

str_char = ''
for i in str_tmp:
    if i != " ":
        str_char += i

list_similar = []

#Loop for calculate a count of similar charecters

for char in str_char:
   if str_char.count(char) > 1:
       list_similar.append(char)

#Calculate a number of distinct char

result = len(str_char) - len(list_similar)

#Print a result

print('Length of entered string: ', len(str_char))
print ('A number of distinct charecters: ', result)