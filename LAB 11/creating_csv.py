import csv

data = [
    ["Dima", "+71234567890"],
    ["Duks", "+79876543210"],
    ["Beka", "+75551234567"]
]

with open("phonebook.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV файл 'phonebook.csv' создан!")