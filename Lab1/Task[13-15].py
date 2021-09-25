#task 13
import math
e=float(input("Enter an engle: "))
e1=math.radians(e)
s=round(math.sin(e1),4)
print("Sine is: ", end="")
print(s)
  
#task 14
p=float(input("Enter a power: "))
a=2**p
s=str(a)[-2:]
print ("Last two digits : ", end="")
print (s)

#task 15
w=float(input("Enter a weight in kilograms: "))
p=round((w*2.20462262185),1)
print("In pounds: ", end="")
print(p)
