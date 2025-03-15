import os

path = input("Enter the path: ")

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print("File is deleted")
    else:
        print("Error")
else:
    print("File is not exists")