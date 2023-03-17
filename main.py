n = input('Eneter your number: ')

a = int(n[0])
b = int(n[1])
c = int(n[2])

print('Sum are: ', a + b + c)


###################################### Another variant###############################


n = input("Enter your number: ")
n = int(n)
 
d1 = n % 10
d2 = n % 100 // 10
d3 = n // 100
 
print("Sum are:", d1 + d2 + d3)
