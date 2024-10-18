# smallest even and larget odd number 
list=[2,4,6,8,1,9,5]
b= 0 
for a in list:
    if a%2!=0:
        if a>b:
            b=a
print("larget odd numer is ",b)
c= 1000000000000000000000
for a in list:
    if a%2==0:
        if a<c:
            c=a
print("smallest even number is ",c)
