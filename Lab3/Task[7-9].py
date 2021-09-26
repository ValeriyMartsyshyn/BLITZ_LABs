#task7
def func():
    a = input("Enter a text sliting a new row with \\n: ")
    print("Number of characters in the text: ", len(a))
    print("Number of words in the text: ", len(a.split()))
    print("Number of lines in the text ", len(a.split('\\n')))

func()

#task8
def func():
    N = input("Enter a number of months: ")
    sum = 300
    if N==0:
        print("Saved money after", N, 'months', sum )
    else:
        for val in range(int(N)):
            if (val + 1)%6 == 0:
                sum = sum + 600
            else:
                sum = sum + 100
        print("Saved money after", N, 'months', sum )        

func()

#task9
def GCD(a,b):
  while b:
    a,b = b, a%b
  return print("Greatest Common Divisor of two numbers", a)



GCD(5,10)
GCD(21,28)
GCD(30,60)
