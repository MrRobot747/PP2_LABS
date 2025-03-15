filename = input("Enter the file name: ")
with open(filename, "r", encoding = "utf-8") as file:
    lines = file.readlines()

num = len(lines)
print(F"Number of lines: {num}")