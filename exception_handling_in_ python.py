#In this code we are demonstrating the exception handling feature of Python

try:
    x = "5" + 5
    y = 5/0
# except TypeError:
#     print("Type Error Occured")
except Exception as e:
    print(e)

print("Hello World") 
# We've printed the above line to demonstrate that try and except let's the control of program to skip to error line and run rest of the code falling after those error lines.
