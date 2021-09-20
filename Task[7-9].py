#task 7:

price = float(input("Enter Price of the meal: $ "))
tip_percent = float(input("Enter tips: % "))

tip = price * (tip_percent/100)
general_sum = price + round(tip, 2)
print('The tip is: $', tip)
print('The total bill: $', general_sum)

#task 8:

from datetime import date
today = date.today()

a = input('Enter a year in format yyyy ')
b = input('Enter a month in format mm ')
c = input('Enter a day in format dd ')

if a.isdigit() and b.isdigit() and c.isdigit():
    year = int(a)
    month = int(b)
    day = int(c)
    if (len(str(year)) == 4) and (month > 0 and month <=12 and len(str(month))<3 and len(str(month))>=1) and ( day > 0 and day <= 31  and len(str(day))<3 and len(str(day))>=1):
        birth_date = date(year, month, day)
        diff =  abs((today - birth_date).days)
        print("Number of days from birth ", diff)
    else:
        print('Wrong format of inputs')
else:
    print('Wrong values of inputs')


#task 9:

value = float(input('Enter an angle between -180 and 180 degrees: '))

if  -180 <= value <= 180:
    print('Your equivalent angle is ', value % 360)
else:
    print('Wrong value of input')
