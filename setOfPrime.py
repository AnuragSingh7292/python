def isPrime(num):
    c=1
    if num == 1:
        c=0
    else:
        for i in range(2,num):
            if num % i == 0:
                c=0
    return c

numbers = list(map(int,input("Enter the max 10 numer : ").split()))

classification = { 'even' : [],'odd':[], 'prime':[]}
for number in numbers:
    if number%2==0 :
        classification['even'].append(number)
    else:
        classification['odd'].append(number)

    if isPrime(number):
        classification['prime'].append(number)

print(classification['even'])
print(classification['odd'])
print(classification ['prime'])

