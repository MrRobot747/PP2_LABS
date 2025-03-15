import re

pattern = r"ab*"
strings = ["aab", "abb", "ab", "aabb"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(f"Match: {s}")
    else:
        print(f"No match: {s}")

    """
No match: aab
Match: abb
Match: ab
No match: aabb""
"""