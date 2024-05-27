import random

user_input = input("Enter the value for endocing or decoding!\n")
user_choice = int(input("Enter 1 for Encoding or 2 for Decoding\n"))

user_input.lower()

encoded_msg=""
decoded_msg=""
match (user_choice):
    case 1:
        #Encoding the message
        if(len(user_input)>=3):
            encoded_msg = user_input[1:] + user_input[0]
            front_rndm_substr = ""
            rear_rndm_substr = ""
            for i in range(0,3):
                front_rndm_substr+= chr(97+random.randint(0,25))
                rear_rndm_substr+=chr(97+random.randint(0,25))
            encoded_msg = front_rndm_substr + encoded_msg + rear_rndm_substr
        else:
            encoded_msg = user_input[::-1] # reversing the string
        print(encoded_msg)
    
    case 2:
        if(len(user_input)>=3):
            decoded_msg = user_input[3:-3]
            decoded_msg = decoded_msg[len(decoded_msg)-1] + decoded_msg[:-1]
        else:
            decoded_msg = user_input[::-1] # reversing the reversed string
        print(decoded_msg)
    
    case _:
        print("Wrong choice!")


