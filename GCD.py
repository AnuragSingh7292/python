
#Greatest Common Divisor using Euclid's algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
#Least Common Multiple
def lcm(a, b):
    return (a * b) // gcd(a, b)

def calculate_lcm(numbers):
    lcmResult = 1
    for num in numbers:
        lcmResult = lcm(lcmResult, num)
    return lcmResult

def calculate_hcf(numbers):
   hcfResult = numbers.pop()
   for num in numbers:
        hcfResult = gcd(hcfResult, num)
   return hcfResult

numbers = {24, 36, 48, 72, 60}
print(type(numbers))
print(f"LCM of  {numbers} : {calculate_lcm(numbers)}")
print(f"HCF of  {numbers} : {calculate_hcf(numbers)}")

