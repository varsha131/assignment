Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 3. # ## Take two number and check whether the sum is greater than 5,less than 5 or equal to 5




a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=a+b
if c>5:
    print("Sum is greater than 5")
elif c<5:
     print("Sum is less than 5")
else:
    print("Sum is equal to 5")