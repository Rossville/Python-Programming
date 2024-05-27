def demo_func():
    user_input = int(input("Enter the number of elements, you want to insert in the given list."))

    demo_lst = []

    while(user_input>0):
        lst_element = int(input("Enter the value"))
        demo_lst.append(lst_element)
        user_input-=1

    #Now we're displaying the result of the list using enumerate function

    for index, value in enumerate(demo_lst):
        print(f"{index+1} -> {value}\n")

if __name__ == "__main__":
    demo_func()