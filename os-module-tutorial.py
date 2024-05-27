import os
import shutil

# print(dir(os))

print(os.getcwd())

# os.mkdir("Sample File - OS module")
os.chdir("C:/Users/Ashutosh/Desktop/Python/Sample File - OS module")
# os.makedirs("subfoler2/subfolder3")

print(os.getcwd())
try:
    # os.removedirs("subfoler2/subfolder3")
    shutil.rmtree("subfoler2/subfolder3")
except Exception as e:
    print(f"There have some error occured while removing some of the files or directories {e}")