import re

def camel_to_snake(camel_str):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str).lower()

camel_text = "helloWorldExample"
snake_text = camel_to_snake(camel_text)
print(snake_text)  
#hello_world_example