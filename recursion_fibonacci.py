def fibonacci(n):
    if(n==0 or n==1):
        return n
    return fibonacci(n-1)+fibonacci(n-2)

user_input = int(input("Enter a number\n"))
print(fibonacci(user_input))