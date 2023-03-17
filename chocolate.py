n = int(input('Enter your number: '))
m = int(input('Enter your number: '))
k = int(input('Enter your number: '))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')