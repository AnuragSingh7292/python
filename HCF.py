# a=12
# b=18
# c=24

a=5
b=15
c=10

d=min(a,b,c)
for i in range(d,1,-1):
    if a%i==0 and b%i==0 and c%i==0:
        print("The hcf is ",i)
        break
  
  
# as list 

def hcf(num):
    n = min(num)
    for i in range(n,1,-1):
        if all(j % i  == 0 for j in num):
            print(i)
            break
lst = [5,10,15]
hcf(lst)


