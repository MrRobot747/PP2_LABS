import re

pattern = r"ab{2,3}"
strings = ["ab", "abb", "aab", "abbb", "abbbbb"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(f"Match: {s}")
    else:
        print(f"No match: {s}")
        """
        No match: ab
Match: abb
No match: aab
Match: abbb
No match: abbbbb"""