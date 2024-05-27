user_input  = input("Enter the value!\nquit")

if user_input != "quit":
    a = int(user_input)
    if(a<5 or a>9):
        raise ValueError("Value should be between 5 and 9")