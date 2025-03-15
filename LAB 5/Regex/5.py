import re

pattern = r"a.*b$"
strings = ["abc", "ab", "asdb", "arfb"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(f"Match: {s}")
    else:
        print(f"No match: {s}")
"""No match: abc
Match: ab
Match: asdb
Match: arfb"""