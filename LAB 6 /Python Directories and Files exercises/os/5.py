rfile = input("Enter the read file: ")
wfile = input("Enter the write file: ")

with open(rfile, "r", encoding = "utf-8") as file1, open(wfile, "w", encoding = "utf-8") as file2:
    file2.write(file1.read())

print("File is copied")