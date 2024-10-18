def forEven(M):
    sum=0
    for i in range(2,M+1,2):
        sum += i
    return sum
def forOdd(N):
    sum=0
    for i in range(1,N+1,2):
        sum += i
    return sum

N,M = map(int,input("Enter the number to N, M : ").split())

print(f"sum of Even {M}th number : {forEven(M)}")
print(f"sum of Odd {N}th number : {forOdd(N)}")

