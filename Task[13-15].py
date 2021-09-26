""" Task 1
A simple way of encrypting a message is to rearrange its characters. One way to rearrange the characters is to pick out
the characters at even indices, put them first in the encrypted string, and follow them by the odd characters.
For example, the string message would be encrypted as msaeesg because the even characters are m, s, a, e (at indices 0, 2, 4, and 6)
and the odd characters are e, s, g (at indices 1, 3, and 5). 

1) Write a function that asks the user for a string and uses this method to encrypt the string.

2) Write a function that decrypts a string that was encrypted with this method. """

#1)

def encrypted():
    message=input("Write your message to encrypt: ")
    e=message[::2] #even
    o=message[1::2] #odd
    return print(e+o)
encrypted()


#2)

def decr():
    message=input("Write your message to decrypt: ")
    length=len(message) #length of the input
    hl=(length+1)//2 #half length
    e=message[:hl]#even 
    o=message[hl:]#odd 
    decrypt=''
    if length%2==0:
        for i in range (hl): #if even
            join=e[i]+o[i]
            decrypt=decrypt+join
    else:
        for i in range (1,hl+1): #if odd
            neparne=i-1 
            join=e[neparne:i]+o[neparne:i]
            decrypt=decrypt+join
    return print(decrypt)
decr()


""" Task 2
Write a function that for 2 given
dictionaries find their common keys. """

def sneakers():
    Shop = {"Nike": "Airmax", "Adidas": "Hoops", "Puma": "Rebound JOY", "New Balance": "574"}
    Client = { "Nike": "Airmax", "Puma": "Rebound JOY"}
    for key in Shop:
        if key in Client:
            print (key, Shop[key])
sneakers()
        

""" Task 3
Create a function which reverts a dictionary
(keys become values, values become keys). """

def to_revert():
    normal = {"Hello": "Python", "I'm": "Bohdan"}
    reverted = {v: k for k, v in normal.items()}
    return print (reverted)
to_revert()
