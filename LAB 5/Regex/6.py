import re

text = "Hello World, How are you?"
new_text = re.sub(r"[ ,.]", ":", text)

print(new_text)
#Hello:World::How:are:you?