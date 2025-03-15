def num_of_letters(s):
    uppercase = 0
    lowercase = 0
    for i in s:
        if i.isupper():
            uppercase += 1
        elif i.islower():
            lowercase += 1
    print(f"Upper: {uppercase}")
    print(f"Lower: {lowercase}")
    print(f"Sum: {uppercase + lowercase}")

s = "Hello, KBTU"
num_of_letters(s)
"""Upper: 5
Lower: 4
Sum: 9"""