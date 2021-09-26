#task 1

nyaam = float (input('enter a length in cm: '))
if nyaam < 0:
    print ('entry is invalid')
else:
    res = nyaam / 2.54 
    print (res, 'inch')


#task 2

whoosh = int (input ('how many credits have you taken? '))
if whoosh > 0 and whoosh < 24:
    print ('congrats, you a freshman!')
elif whoosh > 23 and whoosh < 54:
    print ('congrats, you a sophomore!')
elif whoosh > 53 and whoosh < 84:
    print ('congrats, you a junior!')
elif whoosh > 83:
    print ('congrats, you a senior!')
elif whoosh <= 0:
    print ('you haven\'t any credits, fool')


#task3

from random import randrange 
jeffry = randrange(10)
goat = float (input ('guess the number between 0 n 10: '))
if goat == jeffry:
    print ('you\'re right!')
else:
    print ('that\'s not it, pal')
print (jeffry)
