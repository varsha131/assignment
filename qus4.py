Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 4.# ## Suppose passing marks of a subject is 35.Take input of marks from user and check whether it is greater than passing marks or not




marks=float(input("Enter marks of the student"))
if marks>=35:
    print("Student has passed in the subject")
else:
    print("Student has failed in the subject")