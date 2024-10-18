x=5
y=10
z=15
d=max(x,y,z)
for i in range(d,x*y*z+1):

    if i%x==0 and i%y==0 and i%z==0:
        print("The LCM is ",i)
        break
    
    
# as list 
    
def lcm(numbers):
    mx = max(numbers)
    lt = 1
    for i in numbers:
        lt = lt * i
    for number in range(mx, lt + 1):
        if all(number % i == 0 for i in numbers):
            print(number)
            break

lst = [5, 10, 15]
lcm(lst)
    
    




