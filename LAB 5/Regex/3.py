import re

pattern = r"[a-z]+_[a-z]+"
strings = ["Hello_world", "hello_KBTU", "hello_world", "hello_student"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(f"Match: {s}")
    else:
        print(f"No match: {s}")
        """
No match: Hello_world
No match: hello_KBTU
Match: hello_world
Match: hello_student"""