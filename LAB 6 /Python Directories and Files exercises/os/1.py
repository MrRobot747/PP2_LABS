import os

path = input("Enter the path: ")

if os.path.exists(path):
    print("Path exists")
    print("Files name:", os.path.basename(path))
    print("Folders name:", os.path.dirname(path))
else:
    print("Path not exists")