import re

pattern = r"[A-z]+_[a-z]+"
strings = ["Hello_world", "Hello_KBTU", "Hello_student"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(f"Match: {s}")
    else:
        print(f"No match:  {s}")
""""
"Match: Hello_world
No match:  Hello_KBTU
Match: Hello_student"""