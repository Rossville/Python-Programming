import os

def reading_file(filename):
    f = open(filename,"r")
    print(f.read())
def write_file(filename):
    f = open(filename,"w")
    user_input = input("Start wrting for the file ...\n")
    f.write(user_input)
def append_file(filename):
    f = open(filename,"a")
    user_input = input("Start appending into the file ...\n")
    f.write(" "+user_input)
def create_file():
    user_input_filename = input("Enter the name of the file, you want to create. Give the filename with '.txt' extension at last.\n")
    f = open(user_input_filename,"x")
    
print(os.getcwd())

if os.getcwd() != "C:/Users/Ashutosh/Desktop/Python/Sample File - OS module/subfoler2":
    os.chdir("C:/Users/Ashutosh/Desktop/Python/Sample File - OS module/subfoler2")

# print(os.getcwd())
# The second parameter consists of three parameter like - 'r' -> reading, 'w'-> writing, 'a' -> appending
# 'r' - reads a line (only one line)
# 'w' - it writes into the file by overwriting the previous data.
# 'a' - appending at the last of the previous data
# f.write("hello")

# reading the file
while True:
    user_input  = input('''Enter your mode choice.\n'r' - reading\n'w' - writing\n'a' - appending\n'x - creating the file\n'w' Strictly overwrites the previous content of the file. Enter 'e' to stop the execution.\n''')
    if user_input == "r":
        reading_file("sampleText.txt")
    elif user_input == "w":
        write_file("sampleText.txt")
    elif user_input == "a":
        append_file("sampleText.txt")
    elif user_input == "e":
        break
    elif user_input == "x":
        create_file()
    else:
        print("Wrong Input")
        continue

print("File I/O Operations terminated...")
