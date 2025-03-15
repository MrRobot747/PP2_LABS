import re

def add_space(s):
    return re.sub(r'(?<!^)([A-Z])', r' \1', s)

text = "HelloWorldExample"
print(add_space(text))
#Hello World Example