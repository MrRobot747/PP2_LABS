my_list = ["apple", "banana", "cherry"]
filename = "output.txt"

with open(filename, "w", encoding = "utf-8") as file:
    for i in my_list:
        file.write(i + "\n")

print(f"List in: {filename}")