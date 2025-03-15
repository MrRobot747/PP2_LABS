import string

for i in string.ascii_uppercase:
    filename = f"{i}.txt"
with open(filename, "w") as file:
    file.write(f"This is {filename}\n")
print("File is created")