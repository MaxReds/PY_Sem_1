ticket = input('Enter your ticket number: ')
a = int(ticket[0])
b = int(ticket[1])
c = int(ticket[2])
d = int(ticket[3])
e = int(ticket[4])
f = int(ticket[5])

if a + b + c == d + e + f:
    print('Congratulations - you have a lucky ticket')

else:
    print('Sorry, you are not a winner')
