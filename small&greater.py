num1,num2 = map(int, input("Enter the two number : ").split())
if num1 == num2:
    print(f"{ num1 } is equal to {num2}")
else:
    big = num1 if num1 > num2 else num2
    small = num1 if num1 < num2 else num2
    
    print(f"{big} is greater than {small}")
    print(f"{small} is smaller than {big}")
