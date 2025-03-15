import re

def split_at_uppercase(s):
    return re.split(r'(?=[A-Z])', s)

text = "HelloWorldExample"
print(split_at_uppercase(text))
#['', 'Hello', 'World', 'Example']