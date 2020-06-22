Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5.# ## Write a python function to find max of three numbers




a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a==b==c:
    print("All are equal..No Maximum number")
if (a>b and a>c):
    print("Maximum number is",a)
elif (b>c and b>a):
    print("Maximum number is",b)
else:
    print("Maximum number is",c)