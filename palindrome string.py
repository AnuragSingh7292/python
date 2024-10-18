x =str(input("Enter the string : "))
w = ""
for i in x:
	w = i + w
	
if (x == w):
	print("Yes! it is a palindrome ")
else:
	print("No! it is not palindrome")